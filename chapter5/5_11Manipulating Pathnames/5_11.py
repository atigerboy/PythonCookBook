import os

path = __file__

print( os.path.basename( path ))
print( os.path.dirname( path ) )
print( os.path.join('tmp', 'data', os.path.basename(path)))

path2 = '~/Data/data.csv'
print( os.path.expanduser(path2))#work on WINDOWS Platform!
print( os.path.splitext(path))