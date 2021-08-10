#built-in  round(value, ndigits) function
print( round(1.23, 1) )
print( round(1.25361,3) )
#The number of digits given to  round() can be negative, in which case rounding takes
#place for tens, hundreds, thousands, and so on
print( round( 1627731, -1))
print( round( 1627731, -2))
print( round( 1627731, -3))

x=1.23456
print( format(x, '0.2f') )
print( format(x, '0.3f') )
print( 'value is {:0.3f}'.format(x) )

a = 2.1
b = 4.2

print( a + b )
print( round( a+b , 2))
print( format( a+b, '0.1f'))