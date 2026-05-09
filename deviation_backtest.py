import pandas as pd
import numpy as np
import glob
import os

class DeviationBacktest:
    def __init__(self, data_path='data/'):
        self.data_path = data_path
        # 预设涨跌幅目标 A: 1.2%, B: 1.5%, C: 1.8%
        self.targets = {'A': 0.012, 'B': 0.015, 'C': 0.018}

    def calculate_indicators(self, df):
        """计算策略所需的技术指标"""
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
        # 避免除以0导致的错误
        df['rsi12'] = 100 - (100 / (1 + (gain / loss.replace(0, np.nan))))
        return df

    def run(self):
        # 自动识别 data 目录下的所有 csv 文件
        files = glob.glob(os.path.join(self.data_path, '*.csv'))
        if not files:
            print(f"Error: No CSV files found in {self.data_path}")
            return

        for file_path in files:
            print(f"正在分析: {file_path}")
            df = pd.read_csv(file_path)
            # 统一列名为小写，增强兼容性
            df.columns = df.columns.str.lower()
            df = self.calculate_indicators(df)
            
            file_basename = os.path.basename(file_path)
            file_stats = []

            # 定义信号触发逻辑 (当前K线与前一根K线的交叉判断)
            signals = {
                'MA多头': (df['close'] > df['ma20']) & (df['close'].shift(1) <= df['ma20'].shift(1)),
                'MA空头': (df['close'] < df['ma20']) & (df['close'].shift(1) >= df['ma20'].shift(1)),
                'MACD多头': (df['macd_diff'] > df['macd_dea']) & (df['macd_diff'].shift(1) <= df['macd_dea'].shift(1)),
                'MACD空头': (df['macd_diff'] < df['macd_dea']) & (df['macd_diff'].shift(1) >= df['macd_dea'].shift(1)),
                'RSI多头': (df['rsi12'] < 30) & (df['rsi12'].shift(1) >= 30),
                'RSI空头': (df['rsi12'] > 70) & (df['rsi12'].shift(1) <= 70)
            }

            # 定义区间结束信号 (出现反向信号即停止计算该次偏离)
            exits = {
                'MA多头': signals['MA空头'], 
                'MA空头': signals['MA多头'],
                'MACD多头': signals['MACD空头'], 
                'MACD空头': signals['MACD多头'],
                'RSI多头': (df['rsi12'] > 70), 
                'RSI空头': (df['rsi12'] < 30)
            }

            for name, sig_series in signals.items():
                indices = df.index[sig_series].tolist()
                total = len(indices)
                if total == 0: continue

                hits = {k: 0 for k in self.targets.keys()}
                for idx in indices:
                    # 锚定价格：信号产生后下一根K线的开盘价
                    if idx + 1 >= len(df): continue
                    anchor_price = df.at[idx + 1, 'open']
                    
                    # 寻找该次信号后的第一个反向信号位置
                    future_exits = df.index[(df.index > idx) & exits[name]]
                    end_idx = future_exits[0] if not future_exits.empty else len(df) - 1
                    
                    # 获取计算区间内的最高/最低价
                    window = df.loc[idx+1 : end_idx]
                    if window.empty: continue
                    
                    if '多头' in name:
                        move = (window['high'].max() - anchor_price) / anchor_price
                    else:
                        move = (anchor_price - window['low'].min()) / anchor_price

                    # 检查是否达成 A, B, C 目标
                    for k, threshold in self.targets.items():
                        if move >= threshold: hits[k] += 1

                file_stats.append({
                    '指标': name, 
                    '总触发次数': total,
                    'A率(>1.2%)': f"{hits['A']/total:.2%}",
                    'B率(>1.5%)': f"{hits['B']/total:.2%}",
                    'C率(>1.8%)': f"{hits['C']/total:.2%}"
                })

            # 在 data 文件夹生成对应的同名 .md 报告
            if file_stats:
                report_df = pd.DataFrame(file_stats)
                md_filename = os.path.join(self.data_path, file_basename.replace('.csv', '.md'))
                with open(md_filename, 'w', encoding='utf-8') as f:
                    f.write(f"# {file_basename} 偏离值概率回测分析报告\n\n")
                    # 使用 tabulate 格式美化 Markdown 表格 (需要安装 tabulate 库)
                    f.write(report_df.to_markdown(index=False))
                print(f"成功生成报告: {md_filename}")

if __name__ == "__main__":
    DeviationBacktest().run()
