import pickle

data = [x for x in range(10)]

f = open('data.bin','wb')
pickle.dump(data, f )
f.close()

f = open('data.bin','rb')
data2 = pickle.load(f)
print( data2 )

f = open('somedata', 'wb')
pickle.dump([1, 2, 3, 4], f)
pickle.dump('hello', f)
pickle.dump({'Apple', 'Pear', 'Banana'}, f)
f.close()

f = open('somedata', 'rb')
print( pickle.load(f) )
print( pickle.load(f) )
print( pickle.load(f) )
f.close()


'''
Certain kinds of objects can’t be pickled. These are typically objects that involve some
sort of external system state, such as open files, open network connections, threads,
processes, stack frames, and so forth. User-defined classes can sometimes work around
these limitations by providing  __getstate__() and  __setstate__() methods. If de‐
fined,  pickle.dump() will call  __getstate__() to get an object that can be pickled.
Similarly,  __setstate__() will be invoked on unpickling. To illustrate what’s possible,
here is a class that internally defines a thread but can still be pickled/unpickled:
'''

