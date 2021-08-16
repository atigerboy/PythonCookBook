with open('somefile.bin','wb') as f:
    f.write(b'Hello world') #no \n appended~
    #print(b'hello world', file=f) #error
    f.write('hello world'.encode('ascii'))

with open('somefile.bin','rb') as f:
    data = f.read()

print(data)

import array
nums = array.array('i',[1,2,3,4])
with open('data.bin','wb') as f:
    f.write(nums)

a = array.array('i',[0]*7)
with open('data.bin','rb' ) as f:
    f.readinto( a )

print( a )