import sys
#sys.stdout.write(b'Hello\n')#error, no str
sys.stdout.buffer.write(b'Hello\n')
print('Jalape\u00f1o')