from collections import defaultdict

my_list=['a','b','c','d']
for idx, val in enumerate( my_list ):
    print( idx, val)

for idx, val in enumerate( my_list, 1):
    print( idx, val)

word_summary = defaultdict(list)
with open(__file__) as f:
    lines = f.readlines()

    for idx , line in enumerate( lines ):
        words = [w.strip().lower() for w in line.split()]
        for word in words:
            word_summary[word].append( idx )

print( word_summary )

data = [ (1, 2), (3, 4), (5, 6), (7, 8) ]
#Correct!
for n, (x,y) in enumerate(data):
    print( n , x + y )