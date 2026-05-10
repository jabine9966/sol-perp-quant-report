import pandas as pd
import numpy as np
import glob
import os
import itertools

class ParameterOptimizationStrategy:
    def __init__(self, data_path='data/'):
        self.data_path = data_path
        self.target_pct = 0.015  # 严格执行 1.5% 止盈止损

    def calculate_supertrend(self, df, period, multiplier):
        """计算 SuperTrend 趋势"""
        high, low, close = df['high'], df['low'], df['close']
        tr1 = high - low
        tr2 = abs(high - close.shift(1))
        tr3 = abs(low - close.shift(1))
        tr = pd.concat([tr1, tr2, tr3], axis=1).max(axis=1)
        atr = tr.rolling(period).mean()
        
        hl2 = (high + low) / 2
        upperband = hl2 + (multiplier * atr)
        lowerband = hl2 - (multiplier * atr)
        
        trend = np.ones(len(df))
        for i in range(1, len(df)):
            if close[i] > upperband[i-1]:
                trend[i] = 1
            elif close[i] < lowerband[i-1]:
                trend[i] = -1
            else:
                trend[i] = trend[i-1]
        return trend

    def run_backtest(self, df, long_signals, short_signals):
        """核心回测：多空仓位独立，严格1.5%偏离值"""
        results = {'long': {'win': 0, 'loss': 0}, 'short': {'win': 0, 'loss': 0}}
        
        for side, signals in [('long', long_signals), ('short', short_signals)]:
            indices = df.index[signals].tolist()
            for idx in indices:
                if idx + 1 >= len(df): continue
                # 锚定规则：信号触发后当前K线的开盘价
                anchor_price = df.at[idx + 1, 'open']
                future_df = df.loc[idx+1:]
                
                if side == 'long':
                    tp_price = anchor_price * (1 + self.target_pct)
                    sl_price = anchor_price * (1 - self.target_pct)
                    # 寻找止盈或止损触发点
                    tp_indices = future_df.index[future_df['high'] >= tp_price]
                    sl_indices = future_df.index[future_df['low'] <= sl_price]
                else:
                    tp_price = anchor_price * (1 - self.target_pct)
                    sl_price = anchor_price * (1 + self.target_pct)
                    tp_indices = future_df.index[future_df['low'] <= tp_price]
                    sl_indices = future_df.index[future_df['high'] >= sl_price]
                
                first_tp = tp_indices[0] if not tp_indices.empty else float('inf')
                first_sl = sl_indices[0] if not sl_indices.empty else float('inf')
                
                if first_tp < first_sl:
                    results[side]['win'] += 1
                elif first_sl < first_tp:
                    results[side]['loss'] += 1
        return results

    def run(self):
        csv_files = glob.glob(os.path.join(self.data_path, '*.csv'))
        all_summary_results = []

        for file_path in csv_files:
            fname = os.path.basename(file_path)
            print(f"正在深度分析周期文件: {fname}...")
            df = pd.read_csv(file_path)
            df.columns = df.columns.str.lower()

            # 1. EMA 参数探索
            for f, s in itertools.product(range(7, 22), range(15, 46)):
                if s - f <= 2: continue
                f_ma = df['close'].ewm(span=f, adjust=False).mean()
                s_ma = df['close'].ewm(span=s, adjust=False).mean()
                l_sig = (f_ma > s_ma) & (f_ma.shift(1) <= s_ma.shift(1))
                s_sig = (f_ma < s_ma) & (f_ma.shift(1) >= s_ma.shift(1))
                res = self.run_backtest(df, l_sig, s_sig)
                self._collect(all_summary_results, fname, f"EMA({f},{s})", res)

            # 2. MACD 参数探索
            for sh, lo, mi in itertools.product(range(9, 16), range(20, 36), range(8, 11)):
                if sh >= lo: continue
                diff = df['close'].ewm(span=sh, adjust=False).mean() - df['close'].ewm(span=lo, adjust=False).mean()
                dea = diff.ewm(span=mi, adjust=False).mean()
                l_sig = (diff > dea) & (diff.shift(1) <= dea.shift(1))
                s_sig = (diff < dea) & (diff.shift(1) >= dea.shift(1))
                res = self.run_backtest(df, l_sig, s_sig)
                self._collect(all_summary_results, fname, f"MACD({sh},{lo},{mi})", res)

            # 3. SuperTrend 参数探索
            for p, m in itertools.product(range(9, 13), np.arange(2.0, 3.2, 0.2)):
                m = round(m, 1)
                trend = self.calculate_supertrend(df, p, m)
                l_sig = (pd.Series(trend) == 1) & (pd.Series(trend).shift(1) == -1)
                s_sig = (pd.Series(trend) == -1) & (pd.Series(trend).shift(1) == 1)
                res = self.run_backtest(df, l_sig, s_sig)
                self._collect(all_summary_results, fname, f"SuperTrend({p},{m})", res)

        # 汇总并保存报告
        if all_summary_results:
            report_df = pd.DataFrame(all_summary_results)
            # 过滤负值并排序
            report_df = report_df[report_df['盈亏差值'] >= 0].sort_values(by=['周期', '盈亏差值'], ascending=[True, False])
            
            # 报告文件名与脚本文件名同名
            script_name = os.path.basename(__file__).replace('.py', '.md')
            output_path = os.path.join(self.data_path, script_name)
            
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(f"# 参数寻优汇总报告 ({script_name})\n\n")
                f.write(f"测试目标: 固定偏离值 1.5% | 多空独立持仓\n\n")
                f.write(report_df.to_markdown(index=False))
            print(f"所有周期回测已汇总至: {output_path}")

    def _collect(self, target_list, fname, label, res):
        for side in ['long', 'short']:
            win, loss = res[side]['win'], res[side]['loss']
            if win + loss == 0: continue
            target_list.append({
                '周期': fname, '指标组合': label, '方向': '多头' if side=='long' else '空头',
                '总次数': win + loss, '盈亏比(损:盈)': f"{loss}:{win}", '盈亏差值': win - loss
            })

if __name__ == "__main__":
    ParameterOptimizationStrategy().run()
