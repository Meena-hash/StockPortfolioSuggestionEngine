import stockquotes
import yfinance as yf
from datetime import datetime, timedelta

investment_strategies = {
    "Ethical Investing": {"GILD": 0.2, "FSLR": 0.2, "BYND": 0.2, "TSLA": 0.2, "MSFT": 0.2},
    "Growth Investing": {"AMZN": 0.3, "GOOG": 0.4, "META": 0.3},
    "Index Investing": {"VTI": 0.25, "IXUS": 0.25, "ILTB": 0.25, "SMH": 0.25},
    "Quality Investing": {"XOM": 0.25, "HD": 0.25, "AAPL": 0.3, "TSM": 0.2},
    "Value Investing": {"UNH": 0.2, "BRK.B": 0.2, "JNJ": 0.2, "PG": 0.2, "KO": 0.2}
}


def get_stock_info(stock_ticker):
    return yf.Ticker(stock_ticker)


# get stocks and their weights for distributing money among them
# weights = {"VTI": 0.25, "IXUS": 0.25, "ILTB": 0.25, "SMH": 0.25}
def get_stock_weights(strategy_list):
    stock_weights = {}
    total_strategy_num = len(strategy_list)
    for strategy in strategy_list:
        init_list = investment_strategies[strategy]
        for key, val in init_list.items():
            stock_weights[key] = val / total_strategy_num

    return stock_weights


def get_investment_portfolio(weights, amount):
    portfolio = {}
    for key in weights:
        stock_info = get_stock_info(key)
        portfolio[key] = {}
        portfolio[key]['name'] = stock_info.info['shortName']
        portfolio[key]['symbol'] = key
        portfolio[key]['price'] = stock_info.info['regularMarketPrice']
        portfolio[key]['cost'] = amount * weights[key]
        portfolio[key]['portion'] = weights[key]
        stock_history = {}
        history = stock_info.history(period="5d", interval="1d")['Close']
        for date, closePrice in history.items():
            stock_history[date.date()] = closePrice
        portfolio[key]['stock_history'] = stock_history
    return portfolio


# print(stockquotes.Stock('AAPL'))
# print(get_stock_info("AAPL"))
# print(list(yf.Ticker("AAPL").history(period="1wk", interval="1d")['Close']))
print(get_investment_portfolio(get_stock_weights(['Index Investing']), 10))
