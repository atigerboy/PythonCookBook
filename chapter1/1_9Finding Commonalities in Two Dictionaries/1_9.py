a = {
'x' : 1,
'y' : 2,
'z' : 3
}
b = {
'w' : 10,
'x' : 11,
'y' : 2
}
#find keys in common
print( a.keys() & b.keys() )

#find keys in a not in b, no + operator
print(a.keys() - b.keys() )

#find (key,value) pairs in common !!not values
print(a.items() & b.items() )

c = {key:a[key] for key in  a.keys() & b.keys() }
print(c)