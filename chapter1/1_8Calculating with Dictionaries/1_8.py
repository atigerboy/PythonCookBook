prices = {
'ACME': 45.23,
'AAPL': 612.78,
'IBM': 205.55,
'HPQ': 37.20,
'FB': 10.75
}

min_price = min(zip(prices.values(), prices.keys()))#zip create a literator which only consume !once!
print( min_price )

max_price = max(zip(prices.values(), prices.keys()))
print( max_price )

prices_sorted = sorted(zip(prices.values(), prices.keys()))
print(prices_sorted)

print( min(prices, key=lambda  k:prices[k]))
print( max(prices, key=lambda k:prices[k]))

