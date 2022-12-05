from flask import Flask, request
from StockManager import *

app = Flask(__name__)


@app.route("/stock")
def display_quote():
    symbol = request.args.get('symbol', default="AAPL")
    quote = get_stock_info(symbol)
    return quote.info


if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)
