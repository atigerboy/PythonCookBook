#do test file
import itertools
text=['xajdada','sdfsjkfjs','djdskdasl','dsajdfsj']
with open('somefile.txt','wt',encoding='gbk') as f:
    for x in itertools.combinations_with_replacement( text,4 ):
        print( x, file= f)
