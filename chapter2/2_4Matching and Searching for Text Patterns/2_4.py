text = 'yeah, but no, but yeah, but no, but yeah'
print( text == ' yeah')
print( text.startswith('yeah'))
print( text.endswith('no'))
print(text.find('no'))
print(text.index('no'))

text1 = '11/27/2012'
text2 = 'Nov 27, 2012'
import re
# Simple matching: \d+ means match one or more digits
print( 'yes' if re.match(r'/\d+/\d+/\d+', text1) else 'no')
print('yes' if re.match(r'\d+/\d+/\d+', text2) else 'no')
datepat = re.compile(r'\d+/\d+/\d+')
print( 'yes' if datepat.match(text1 ) else 'no')
print( 'yes' if datepat.match( text2 ) else 'no')

text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
print( datepat.findall( text ))
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
m = datepat.match('11/27/2012')
[ print( m.group(i+1)) for i in range(len(m.groups()))]

for month, day, year in datepat.findall(text):
    print('{}-{}-{}'.format(year, month, day))
for m in datepat.finditer(text):
    print(m.groups())