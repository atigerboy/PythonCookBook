s = 'pýtĥöñ\fis\tawesome\r\n'

remap = {
 ord('\t') : ' ',
 ord('\f') : ' ',
 ord('\r') : None # Deleted
 }

a = s.translate( remap )
print( a )

import unicodedata
import sys
cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode) if unicodedata.combining(chr(c)))
print( cmb_chrs )
b = unicodedata.normalize('NFD', a)
print( b )

print( b.translate( cmb_chrs ))

digitmap = { c: ord('0') + unicodedata.digit(chr(c))
for c in range(sys.maxunicode)
if unicodedata.category(chr(c)) == 'Nd' }

print( len( digitmap ))
x = '\u0661\u0662\u0663'
print( x.translate(digitmap) )

b = unicodedata.normalize('NFD', a)
print( b.encode('ascii', 'ignore').decode('ascii') )