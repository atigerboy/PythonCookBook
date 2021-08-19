import io
import sys
import urllib.request
import os

u = urllib.request.urlopen('http://www.python.org')
f = io.TextIOWrapper( u, encoding='utf-8')
text = f.read()
f.close()

print( text[0:18] )

print( sys.stdout.encoding )
sys.stdout = io.TextIOWrapper( sys.stdout.detach(), encoding='latin-1')
print( sys.stdout.encoding )

#print("测试中文看显示") #error了， 解析不了中文
sys.stdout = io.TextIOWrapper( sys.stdout.detach(), encoding='UTF-8')
print("测试中文看显示")