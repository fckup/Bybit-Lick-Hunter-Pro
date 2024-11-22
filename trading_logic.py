import pandas as pd
import numpy as np

def analyze_market_data(data):
    df = pd.DataFrame(data, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    df['sma_10'] = df['close'].rolling(window=10).mean()
    df['sma_50'] = df['close'].rolling(window=50).mean()
    df['signal'] = np.where(df['sma_10'] > df['sma_50'], 1, 0)
    df['position'] = df['signal'].diff()
    return df

def execute_trade(exchange, symbol, position, amount=0.01):
    if position == 1:
        create_order(exchange, symbol, 'buy', amount)
    elif position == -1:
        create_order(exchange, symbol, 'sell', amount)
