from operator import itemgetter

stocks = [
    {'ticker': 'APPL', 'price': 201},
    {'ticker': 'GOOG', 'price': 800},
    {'ticker': 'f', 'price': 43},
    {'ticker': 'MSFT', 'price': 342},
    {'ticker': 'TUNA', 'price': 34},
]

for x in sorted(stocks, key= itemgetter('ticker')):
    print(x)

print('-------------------------------------------')
for x in sorted(stocks, key=itemgetter('ticker','price')):
    print(x)
