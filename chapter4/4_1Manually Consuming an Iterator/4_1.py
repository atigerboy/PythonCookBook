with open('./test.txt') as f:
    try:
        while True:
            line  = next(f) #next(f, None) to avoid exception
            print( line, end='')
    except StopIteration:
        print()
        pass


items = [1, 2, 3]
it = iter( items )
print( next( it,None ) )
print( next( it, None) )
print( next( it, None))
print( next( it, None))
