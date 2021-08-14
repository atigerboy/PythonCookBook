import os
import fnmatch
import re
import hashlib

def gen_find( filepat, top):
    for path, dirlist, filelist in os.walk(top):
        for name in fnmatch.filter( filelist, filepat):
            yield os.path.join(path, name)

def gen_opener( filenames ):
    for filename in filenames:
        f = open(filename,'rt', encoding='gbk', errors='ignore')#file coding error
        yield  f
        f.close()

def gen_concatenate( iterators ):
    for it in iterators:
        yield from it

def gen_grep(pattern, lines):
    pat = re.compile(pattern)
    for line in lines:
        if pat.search( line ):
            yield  line


pynames = gen_find('[0-9]*_[0-9]*.py','../../..')
files = gen_opener( pynames )
lines = gen_concatenate( files )
pylines = gen_grep('(?:import)', lines)
for line in pylines:
    print(line, end='')