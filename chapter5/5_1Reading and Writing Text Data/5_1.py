#do test file
import itertools
text=['xajdada','sdfsjkfjs','djdskdasl','dsajdfsj']
with open('somefile.txt','wt',encoding='gbk') as f:
    for x in itertools.combinations_with_replacement( text,4 ):
        f.write('{!r}\n'.format( x ) )

#read
with open('somefile.txt','rt',encoding='ascii', errors='ignore') as f:
    for line in f:
        print( line,end='')