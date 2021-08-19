import os
names = os.listdir('..')

print( names )

import os.path

names = [name for name in os.listdir('../..') if os.path.isfile( os.path.join('..', name))]
print( names )

import glob
pyfiles = glob.glob('../*.py')
print(pyfiles)

from fnmatch import  fnmatch
pyfiles = [ name for name in os.listdir('..') if fnmatch(name, '*.py')]
print( pyfiles )

