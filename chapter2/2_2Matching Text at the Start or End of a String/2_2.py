# -*- coding: utf-8 -*-

filename = 'spam.txt'
print( filename.endswith('.txt'))
print( filename.startswith('file:'))

url = 'http://www.python.org'
print( url.startswith(('https','http','ftp')))

from urllib.request import urlopen

def read_data(name:str):
    if name.startswith(('http:','https:','ftp:')):
        return urlopen(name).read()
    else:
        with open(name) as f:
            return f.read()
import os
filenames = os.listdir('.')
print(filenames)
print(read_data(url))
print(read_data(filenames[0]))

