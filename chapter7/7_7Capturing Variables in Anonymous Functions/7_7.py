#use vars in function body
x = 10
a = lambda  y:x+y
print( a(10 )) #20
x = 20
print( a(20) ) #40

#capture while define function
x = 10
a = lambda  y, x = x: x+y #same as function default Arguments
print( a(10 )) #20
x = 20
print( a(20) ) #30

funcs = [lambda x: x+n for n in range(5)] #get final n
for f in funcs:
    print( f(0) )

funcs = [ lambda  x, n=n: x+n for n in range(5)] #function default arguments
for f in funcs:
    print( f(0) )
