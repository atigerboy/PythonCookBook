import sys

p=(4,5)
x,y=p
print(x, y)
data=['ACME',50, 91.1,(2012,12,21)]
name,shares,price,date = data
print(name, date)
name,shares,price,(year, mon, day) = data
print(name, year, mon, day)

# mismatch the number of elements
try:
    p = (4,5)
    x,y,z=p
except Exception as err:
    print(err)

s='Hello'
a,b,c,d,e=s
print(a,b,c,e)

#discard certain values

_,shares,price,_=data
print(shares, price)

a,b,*c=range(1,10,2)
print(a, c)