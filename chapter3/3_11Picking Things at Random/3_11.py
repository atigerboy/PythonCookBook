import random

values = [1, 2, 3, 4, 5, 6]
print( random.choice( values ))
print( random.sample( values, 2 ))
random.shuffle( values )
print( values )

print( random.randint( 0,10))
print( random.random() )
print( random.getrandbits( 200 ))

random.seed()
print( random.getrandbits( 200 ))
print( random.getrandbits( 200 ))

random.seed(12345)
print( random.getrandbits( 200 ))
print( random.getrandbits( 200 ))

random.seed(12345)
print( random.getrandbits( 200 ))
print( random.getrandbits( 200 ))

random.seed(b'bytedata') # Seed based on byte data