stocks = {
    'APPL': 201,
    'GOOG': 800,
    'YAHOO': 43,
    'MSFT': 342,
    'TICKER' : 34,
}

# print(min(stocks))

# (342, GOOG) (434 , APPL)
min_price = min(zip(stocks.values(), stocks.keys()))
print(min_price)