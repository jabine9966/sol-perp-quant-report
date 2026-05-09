import pandas as pd
import numpy as np
import glob
import os

class DeviationStrategy:
    def __init__(self, data_path='data/'):
        self.data_path = data_path
        self.targets = [0.012, 0.015, 0.018]  # A, B, C 目标

    def calculate_indicators(self, df):
        # MA20
        df['ma20'] = df['close'].rolling(window=20).mean()
        # MACD
        ema12 = df['close'].ewm(span=12, adjust=False).mean()
        ema26 = df['close'].ewm(span=26, adjust=False).mean()
        df['macd_diff'] = ema12 - ema26
        df['macd_dea'] = df['macd_diff'].ewm(span=9, adjust=False).mean()
        # RSI12
        delta = df['close'].diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=12).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=12).mean()
        df['rsi12'] = 100 - (100 / (1 + (gain / loss)))
        return df

    def run(self):
        files = glob.glob(os.path.join(self.data_path, '*.csv'))
        all_stats = []

        for file in files:
            df = pd.read_csv(file)
            df.columns = df.columns.str.lower()
            df = self.calculate_indicators(df)
            interval_name = os.path.basename(file)

            # 定义信号
            signals = {
                'MA多头': (df['close'] > df['ma20']) & (df['close'].shift(1) <= df['ma20'].shift(1)),
                'MA空头': (df['close'] < df['ma20']) & (df['close'].shift(1) >= df['ma20'].shift(1)),
                'MACD多头': (df['macd_diff'] > df['macd_dea']) & (df['macd_diff'].shift(1) <= df['macd_dea'].shift(1)),
                'MACD空头': (df['macd_diff'] < df['macd_dea']) & (df['macd_diff'].shift(1) >= df['macd_dea'].shift(1)),
                'RSI多头': (df['rsi12'] < 30) & (df['rsi12'].shift(1) >= 30),
                'RSI空头': (df['rsi12'] > 70) & (df['rsi12'].shift(1) <= 70)
            }

            # 定义反向退出信号（用于确定偏离值计算区间）
            exits = {
                'MA多头': signals['MA空头'], 'MA空头': signals['MA多头'],
                'MACD多头': signals['MACD空头'], 'MACD空头': signals['MACD多头'],
                'RSI多头': (df['rsi12'] > 70), 'RSI空头': (df['rsi12'] < 30)
            }

            for name, sig_series in signals.items():
                sig_indices = df.index[sig_series].tolist()
                total = len(sig_indices)
                if total == 0: continue

                counts = [0, 0, 0] # A, B, C 计数
                for idx in sig_indices:
                    if idx + 1 >= len(df): continue
                    anchor_price = df.at[idx + 1, 'open']
                    
                    # 寻找下一个退出信号位置
                    future_exits = df.index[(df.index > idx) & exits[name]]
                    end_idx = future_exits[0] if not future_exits.empty else len(df) - 1
                    
                    window = df.loc[idx+1 : end_idx]
                    if '多头' in name:
                        max_dev = (window['high'].max() - anchor_price) / anchor_price
                    else:
                        max_dev = (anchor_price - window['low'].min()) / anchor_price

                    for i, t in enumerate(self.targets):
                        if max_dev >= t: counts[i] += 1

                all_stats.append({
                    'File': interval_name, 'Indicator': name, 'Total': total,
                    'A_Rate': f"{counts[0]/total:.2%}", 'B_Rate': f"{counts[1]/total:.2%}", 'C_Rate': f"{counts[2]/total:.2%}"
                })

        report = pd.DataFrame(all_stats)
        report.to_csv('final_report.csv', index=False)
        print(report.to_markdown()) # 在Action日志中直接打印美化表格

if __name__ == "__main__":
    DeviationStrategy().run()
