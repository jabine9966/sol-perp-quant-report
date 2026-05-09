import pandas as pd
import numpy as np
import glob
import os

class DeviationBacktest:
    def __init__(self, data_path='data/'):
        self.data_path = data_path
        self.targets = {'A': 0.012, 'B': 0.015, 'C': 0.018}

    def calculate_indicators(self, df):
        df['ma20'] = df['close'].rolling(window=20).mean()
        ema12 = df['close'].ewm(span=12, adjust=False).mean()
        ema26 = df['close'].ewm(span=26, adjust=False).mean()
        df['macd_diff'] = ema12 - ema26
        df['macd_dea'] = df['macd_diff'].ewm(span=9, adjust=False).mean()
        delta = df['close'].diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=12).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=12).mean()
        df['rsi12'] = 100 - (100 / (1 + (gain / loss.replace(0, np.nan))))
        return df

    def run(self):
        files = glob.glob(os.path.join(self.data_path, '*.csv'))
        if not files:
            print(f"Error: No CSV files found in {self.data_path}")
            return

        all_file_stats = [] # 用于存放所有周期的汇总数据

        for file_path in files:
            print(f"正在分析: {file_path}")
            df = pd.read_csv(file_path)
            df.columns = df.columns.str.lower()
            df = self.calculate_indicators(df)
            file_basename = os.path.basename(file_path)

            signals = {
                'MA多头': (df['close'] > df['ma20']) & (df['close'].shift(1) <= df['ma20'].shift(1)),
                'MA空头': (df['close'] < df['ma20']) & (df['close'].shift(1) >= df['ma20'].shift(1)),
                'MACD多头': (df['macd_diff'] > df['macd_dea']) & (df['macd_diff'].shift(1) <= df['macd_dea'].shift(1)),
                'MACD空头': (df['macd_diff'] < df['macd_dea']) & (df['macd_diff'].shift(1) >= df['macd_dea'].shift(1)),
                'RSI多头': (df['rsi12'] < 30) & (df['rsi12'].shift(1) >= 30),
                'RSI空头': (df['rsi12'] > 70) & (df['rsi12'].shift(1) <= 70)
            }

            exits = {
                'MA多头': signals['MA空头'], 'MA空头': signals['MA多头'],
                'MACD多头': signals['MACD空头'], 'MACD空头': signals['MACD多头'],
                'RSI多头': (df['rsi12'] > 70), 'RSI空头': (df['rsi12'] < 30)
            }

            for name, sig_series in signals.items():
                indices = df.index[sig_series].tolist()
                total = len(indices)
                if total == 0: continue

                hits = {k: 0 for k in self.targets.keys()}
                for idx in indices:
                    if idx + 1 >= len(df): continue
                    anchor_price = df.at[idx + 1, 'open']
                    future_exits = df.index[(df.index > idx) & exits[name]]
                    end_idx = future_exits[0] if not future_exits.empty else len(df) - 1
                    window = df.loc[idx+1 : end_idx]
                    if window.empty: continue
                    
                    move = (window['high'].max() - anchor_price) / anchor_price if '多头' in name else \
                           (anchor_price - window['low'].min()) / anchor_price

                    for k, threshold in self.targets.items():
                        if move >= threshold: hits[k] += 1

                all_file_stats.append({
                    '周期': file_basename,
                    '指标': name,
                    '触发次数': total,
                    'A率(>1.2%)': f"{hits['A']/total:.2%}",
                    'B率(>1.5%)': f"{hits['B']/total:.2%}",
                    'C率(>1.8%)': f"{hits['C']/total:.2%}"
                })

        # --- 核心改动：汇总成一个 .md 文件 ---
        if all_file_stats:
            summary_df = pd.DataFrame(all_file_stats)
            # 按周期和指标排序，方便对比
            summary_df = summary_df.sort_values(by=['周期', '指标'])
            md_filename = os.path.join(self.data_path, 'multi_timeframe_report.md')
            with open(md_filename, 'w', encoding='utf-8') as f:
                f.write("# 全周期偏离值概率汇总回测报告\n\n")
                f.write(f"生成时间: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
                f.write(summary_df.to_markdown(index=False))
            print(f"成功汇总所有结果至: {md_filename}")

if __name__ == "__main__":
    DeviationBacktest().run()
