from flask import Flask, request
from StockManager import *

app = Flask(__name__)

portfolio = []

def is_stock_in_portfolio():
    return {}

def update_portfolio(symbol, price, quantity):
    updated = False
    #print(portfolio)
    if len(portfolio) > 0:
        for invested_stock in portfolio:
            if invested_stock['stock'] == symbol:
                old_price = invested_stock['price']
                old_quantity = invested_stock['quantity']
                new_price = (old_price*old_quantity + price*quantity)/ (old_quantity+quantity)
                new_quantity = old_quantity + quantity
                invested_stock['price'] = round(new_price, 2)
                invested_stock['quantity'] = new_quantity
                updated = True
    if not updated:
        new_added_stock = {'stock':symbol, 'price':round(price, 2), 'quantity':quantity}
        portfolio.append(new_added_stock)
    print(portfolio)

@app.route('/stock')
def display_quote():
    symbol = request.args.get('symbol', default="AAPL")
    quote = get_stock_info(symbol)
    return quote.info

# return portfolio details in GET and buy stocks in POST
# Sample Request for POST
# {
#    "stocks" : 
#    [
#         { 
#             "stock":"APPL",
#             "quantity": 3,
#             "price": 350
#         },
#         { 
#             "stock":"AMZN",
#             "quantity": 5,
#             "price": 200
#         }
#     ]
# }
@app.route('/investment', methods=['GET', 'POST'])
def investment():
    if request.method == 'GET':
        response = {'portfolio':portfolio}
    else:
        buy_stocks = request.json
        count = 0
        for stock in buy_stocks['stocks']:
            print(stock)
            stock_symbol = stock['stock']
            stock_quantity = stock['quantity']
            stock_price = stock['price']
            update_portfolio(stock_symbol, stock_price, stock_quantity)
            count+=1
        response = {'success':count!=0}
    return response

# get stock recommendation based on investment strategies and amount (default investment amount is 5000)
# sample cURL request for fetching recommendation based on two strategies
# curl --location --request GET 'http://localhost:5000/recommendation?amount=10000&strategies=Index Investing,Ethical Investing' \
# --header 'Content-Type: application/json' \
# --data-raw '{   
#    "stocks" : 
#    [
#         { 
#             "stock":"APPL",
#             "quantity": 3,
#             "price": 350
#         },
#         { 
#             "stock":"AMZN",
#             "quantity": 5,
#             "price": 200
#         }
#     ]
# }'
@app.route('/recommendation', methods=['GET'])
def get_stock_recommendation():
    investment_amount = int(request.args.get('amount', 5000))
    list_of_strategies = request.args.get('strategies')
    print(list_of_strategies.split(','))
    stock_weights = get_stock_weights(list_of_strategies.split(','))
    recommendation = get_investment_portfolio(stock_weights, investment_amount)
    return recommendation

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)
