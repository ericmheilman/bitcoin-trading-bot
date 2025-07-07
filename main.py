import ccxt

if __name__ == "__main__":
    exchange = ccxt.binance()
    ticker = exchange.fetch_ticker('BTC/USDT')
    print(f"Current BTC/USDT price on Binance: {ticker['last']}")
