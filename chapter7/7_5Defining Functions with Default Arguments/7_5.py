def spam( a, b=42):
    print( a, b)

spam(1)
spam(1,2)

x = 42
def spam( a, b=x): #capture while defining
    print( a, b )

spam(1)
x = 23  #has no effect
spam(1)

def spam(a, b=[]):
    print(b)
    return b

x = spam(1)
x.append(99)
x.append('Yow!')
print( x )
spam(1) #Modified list gets returns (still x)

def spam(a, b=None):
    if  not b :
        b = []
    print( b )
    return b
x = spam(1)
x.append(99)
x.append('Yow!')
print(x)
spam(1) #still new array