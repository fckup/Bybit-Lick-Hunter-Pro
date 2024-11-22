import time
from config import load_config
from logger import setup_logger
from utils import init_exchange, fetch_market_data
from trading_logic import analyze_market_data, execute_trade

logger = setup_logger()

def main():
    config = load_config()
    exchange = init_exchange(config)
    symbol = config['symbol']
    timeframe = config.get('timeframe', '1m')
    limit = config.get('limit', 100)
    sleep_interval = config.get('sleep_interval', 60)  # in seconds

    while True:
        try:
            data = fetch_market_data(exchange, symbol, timeframe, limit)
            if data is not None:
                df = analyze_market_data(data)
                last_position = df['position'].iloc[-1]
                if last_position != 0:
                    execute_trade(exchange, symbol, last_position, config['trade_amount'])
        except Exception as e:
            logger.error(f'Unexpected error: {e}')
        time.sleep(sleep_interval)

if __name__ == '__main__':
    main()
