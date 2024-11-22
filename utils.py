import ccxt
import time

def init_exchange(config):
    exchange = ccxt.bybit({
        'apiKey': config['api_key'],
        'secret': config['api_secret'],
        'enableRateLimit': True,
    })
    return exchange

def fetch_market_data(exchange, symbol, timeframe='1m', limit=100):
    try:
        ohlcv = exchange.fetch_ohlcv(symbol, timeframe=timeframe, limit=limit)
        return ohlcv
    except ccxt.BaseError as e:
        logger.error(f'Error fetching market data: {e}')
        return None

def create_order(exchange, symbol, side, amount):
    try:
        if side == 'buy':
            order = exchange.create_market_buy_order(symbol, amount)
        elif side == 'sell':
            order = exchange.create_market_sell_order(symbol, amount)
        logger.info(f'Created {side} order for {amount} {symbol}: {order}')
        return order
    except ccxt.BaseError as e:
        logger.error(f'Error creating {side} order: {e}')
        return None
