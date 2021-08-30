'''lambda for inline,anonymous'''
add = lambda  x, y: x+y
print( help(add) )
print( add( 2, 3) )
print( add( 'hello', 'world'))

names = ['David Beazley', 'Brian Jones','Raymond Hettinger', 'Ned Batchelder']

sorted( names, key=lambda  name:name.split()[-1].lower())
print( names )