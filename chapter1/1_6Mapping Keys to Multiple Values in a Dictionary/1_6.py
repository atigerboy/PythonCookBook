from collections import defaultdict
d = defaultdict(list)#list type
d['a'].append(1) #facade pattern
d['a'].append(2)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)

print(d['a'],d['b'])

d = defaultdict(set)#set type
d['a'].add(1)
d['a'].add(2)
d['a'].add(1)
d['a'].add(2)
d['b'].add(4)

print(d['a'],d['b'])