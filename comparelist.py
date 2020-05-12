import heapq

grades = [32 , 43 , 434, 324, 234, 234 ,42, 45, 21]

print(heapq.nlargest(3, grades))


stocks = [
    {'ticker': 'APPL', 'price': 201},
    {'ticker': 'GOOG', 'price': 800},
    {'ticker': 'f', 'price': 43},
    {'ticker': 'MSFT', 'price': 342},
    {'ticker': 'TUNA', 'price': 34},
]

print(heapq.nsmallest(2, stocks, key=lambda  stock: stock['price']))
