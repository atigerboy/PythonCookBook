nums = [1, 2, 3, 4, 5]
s = sum( x * x for x in nums )
print( s )
s = sum([x * x for x in nums])#slower one
print(s)

import  os
files = os.listdir('..')
if any( name.endswith('.py') for name in files ):
    print(f'There be python ') #reference to name failed
else:
    print( 'sorry, no python')

# Output a tuple as CSV
s = ('ACME', 50, 123.45)
print(','.join(str(x) for x in s))

# Data reduction across fields of a data structure
portfolio = [
{'name':'GOOG', 'shares': 50},
{'name':'YHOO', 'shares': 75},
{'name':'AOL', 'shares': 20},
{'name':'SCOX', 'shares': 65}
]
print(  min(s['shares'] for s in portfolio) )

# Original: Returns 20
min_shares = min(s['shares'] for s in portfolio) #select shares
print( min_shares )

# Alternative: Returns {'name': 'AOL', 'shares': 20}
min_shares = min(portfolio, key=lambda s: s['shares'])#select *
print( min_shares )