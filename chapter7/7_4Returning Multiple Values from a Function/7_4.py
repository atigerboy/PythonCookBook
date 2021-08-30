def myfun():
    return 1,2,3

a, b, c =myfun()
print(a, b, c)
print( help( myfun ) )
a = ( 1, 2)
b = 1,2
print( a == b )
a, _,_ =  myfun()
print( a )