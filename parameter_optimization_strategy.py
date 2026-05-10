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
        high, low, close = df['high'], df['low'], df['close']
        tr = pd.concat([high - low, abs(high - close.shift(1)), abs(low - close.shift(1))], axis=1).max(axis=1)
        atr = tr.rolling(period).mean()
        hl2 = (high + low) / 2
        upperband, lowerband = hl2 + (multiplier * atr), hl2 - (multiplier * atr)
        trend = np.ones(len(df))
        for i in range(1, len(df)):
            if close[i] > upperband[i-1]: trend[i] = 1
            elif close[i] < lowerband[i-1]: trend[i] = -1
            else: trend[i] = trend[i-1]
        return trend

    def run_backtest(self, df, long_signals, short_signals):
        results = {'long': {'win': 0, 'loss': 0}, 'short': {'win': 0, 'loss': 0}}
        for side, signals in [('long', long_signals), ('short', short_signals)]:
            indices = df.index[signals].tolist()
            for idx in indices:
                if idx + 1 >= len(df): continue
                anchor = df.at[idx + 1, 'open']
                future = df.loc[idx+1:]
                if side == 'long':
                    tp_i = future.index[future['high'] >= anchor * (1 + self.target_pct)]
                    sl_i = future.index[future['low'] <= anchor * (1 - self.target_pct)]
                else:
                    tp_i = future.index[future['low'] <= anchor * (1 - self.target_pct)]
                    sl_i = future.index[future['high'] >= anchor * (1 + self.target_pct)]
                f_tp = tp_i[0] if not tp_i.empty else float('inf')
                f_sl = sl_i[0] if not sl_i.empty else float('inf')
                if f_tp < f_sl: results[side]['win'] += 1
                elif f_sl < f_tp: results[side]['loss'] += 1
        return results

    def run(self):
        csv_files = glob.glob(os.path.join(self.data_path, '*.csv'))
        all_raw_data = []

        for file_path in csv_files:
            fname = os.path.basename(file_path)
            print(f"正在深度分析周期文件: {fname}...")
            df = pd.read_csv(file_path).rename(columns=str.lower)

            # --- 核心寻优循环 ---
            # 1. EMA
            for f, s in itertools.product(range(7, 22), range(15, 46)):
                if s - f <= 2: continue
                l_s = (df['close'].ewm(span=f).mean() > df['close'].ewm(span=s).mean()) & (df['close'].ewm(span=f).mean().shift(1) <= df['close'].ewm(span=s).mean().shift(1))
                s_s = (df['close'].ewm(span=f).mean() < df['close'].ewm(span=s).mean()) & (df['close'].ewm(span=f).mean().shift(1) >= df['close'].ewm(span=s).mean().shift(1))
                res = self.run_backtest(df, l_s, s_s)
                self._record(all_raw_data, fname, "EMA", f"{f},{s}", res)

            # 2. MACD
            for sh, lo, mi in itertools.product(range(9, 16), range(20, 36), range(8, 11)):
                if sh >= lo: continue
                diff = df['close'].ewm(span=sh).mean() - df['close'].ewm(span=lo).mean()
                dea = diff.ewm(span=mi).mean()
                l_s, s_s = (diff > dea) & (diff.shift(1) <= dea.shift(1)), (diff < dea) & (diff.shift(1) >= dea.shift(1))
                res = self.run_backtest(df, l_s, s_s)
                self._record(all_raw_data, fname, "MACD", f"{sh},{lo},{mi}", res)

            # 3. SuperTrend
            for p, m in itertools.product(range(9, 13), np.arange(2.0, 3.2, 0.2)):
                m = round(m, 1)
                t = self.calculate_supertrend(df, p, m)
                l_s, s_s = (pd.Series(t)==1)&(pd.Series(t).shift(1)==-1), (pd.Series(t)==-1)&(pd.Series(t).shift(1)==1)
                res = self.run_backtest(df, l_s, s_s)
                self._record(all_raw_data, fname, "SuperTrend", f"{p},{m}", res)

        # --- 报告生成逻辑 ---
        full_df = pd.DataFrame(all_raw_data)
        script_name = os.path.basename(__file__).replace('.py', '.md')
        
        with open(os.path.join(self.data_path, script_name), 'w', encoding='utf-8') as f:
            f.write(f"# 参数寻优汇总报告 ({script_name})\n\n")
            
            # 1. 生成共振列表
            f.write("## 🟢 多空共振参数列表 (同一指标参数在多空方向盈亏差均 > 0)\n\n")
            resonance = []
            for (file, indicator, params), group in full_df.groupby(['周期', '指标类型', '参数组合']):
                if len(group) == 2 and (group['盈亏差值'] > 0).all():
                    resonance.append({
                        '周期': file, '指标': f"{indicator}({params})",
                        '多头差值': group[group['方向']=='多头']['盈亏差值'].values[0],
                        '空头差值': group[group['方向']=='空头']['盈亏差值'].values[0],
                        '共振总差值': group['盈亏差值'].sum()
                    })
            if resonance:
                f.write(pd.DataFrame(resonance).sort_values('共振总差值', ascending=False).to_markdown(index=False) + "\n\n")
            else:
                f.write("暂无符合条件的共振参数。\n\n")

            # 2. 生成各指标 Top 20 详情
            f.write("## 📊 指标优选详情 (各指标各方向仅保留 Top 20)\n\n")
            top_20_df = full_df[full_df['盈亏差值'] > 0].groupby(['周期', '指标类型', '方向']).apply(lambda x: x.nlargest(20, '盈亏差值')).reset_index(drop=True)
            f.write(top_20_df.to_markdown(index=False))

    def _record(self, data_list, fname, itype, params, res):
        for side in ['long', 'short']:
            w, l = res[side]['win'], res[side]['loss']
            if w + l > 0:
                data_list.append({'周期': fname, '指标类型': itype, '参数组合': params, '方向': '多头' if side=='long' else '空头', '锚定次数': w+l, '盈亏比(损:盈)': f"{l}:{w}", '盈亏差值': w-l})

if __name__ == "__main__":
    ParameterOptimizationStrategy().run()
