import pandas as pd
import numpy as np
import glob
import os

class DeviationBacktest:
    def __init__(self, data_path='data/'):
        self.data_path = data_path
        self.targets = {'A': 0.012, 'B': 0.015, 'C': 0.018}

    def calculate_indicators(self, df):
        # MA20
        df['ma20'] = df['close'].rolling(window=20).mean()
        # MACD (12, 26, 9)
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
        if not files:
            print("错误: data/ 目录下未找到 CSV 文件")
            return

        all_stats = []
        for file in files:
            df = pd.read_csv(file)
            df.columns = df.columns.str.lower()
            df = self.calculate_indicators(df)
            interval = os.path.basename(file)

            # 信号定义
            signals = {
                'MA多头': (df['close'] > df['ma20']) & (df['close'].shift(1) <= df['ma20'].shift(1)),
                'MA空头': (df['close'] < df['ma20']) & (df['close'].shift(1) >= df['ma20'].shift(1)),
                'MACD多头': (df['macd_diff'] > df['macd_dea']) & (df['macd_diff'].shift(1) <= df['macd_dea'].shift(1)),
                'MACD空头': (df['macd_diff'] < df['macd_dea']) & (df['macd_diff'].shift(1) >= df['macd_dea'].shift(1)),
                'RSI多头': (df['rsi12'] < 30) & (df['rsi12'].shift(1) >= 30),
                'RSI空头': (df['rsi12'] > 70) & (df['rsi12'].shift(1) <= 70) # 已修正逻辑
            }

            # 对应退出信号（用于确定计算区间）
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
                    anchor_price = df.at[idx + 1, 'open'] # 下一根开盘锚定
                    
                    # 确定终点
                    future_exits = df.index[(df.index > idx) & exits[name]]
                    end_idx = future_exits[0] if not future_exits.empty else len(df) - 1
                    
                    window = df.loc[idx+1 : end_idx]
                    move = (window['high'].max() - anchor_price) / anchor_price if '多头' in name else \
                           (anchor_price - window['low'].min()) / anchor_price

                    for k, threshold in self.targets.items():
                        if move >= threshold: hits[k] += 1

                all_stats.append({
                    '文件': interval, '指标': name, '总数': total,
                    'A率(>1.2%)': f"{hits['A']/total:.2%}",
                    'B率(>1.5%)': f"{hits['B']/total:.2%}",
                    'C率(>1.8%)': f"{hits['C']/total:.2%}"
                })

        report = pd.DataFrame(all_stats)
        report.to_csv('deviation_report.csv', index=False, encoding='utf-8-sig')
        # 直接输出 Markdown 到 GitHub Action 日志
        print(report.to_markdown(index=False))

if __name__ == "__main__":
    DeviationBacktest().run()
