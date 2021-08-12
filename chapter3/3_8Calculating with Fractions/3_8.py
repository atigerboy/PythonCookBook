from fractions import  Fraction

a = Fraction(5,4)
b = Fraction(7,16)
print( a+b,a-b,a*b, a/b, a>b)
c = a * b
print( c, c.numerator, c.denominator )

print( float(c))

print(c.limit_denominator(8))
d = c.limit_denominator(8)
print( c<d, d, c )
x = 3.75
y = Fraction( *x.as_integer_ratio() )
print( y )