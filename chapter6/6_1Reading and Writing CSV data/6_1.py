import csv
import re

with open('stocks.csv') as f:
    f_csv = csv.reader(f)
    headers = next( f_csv )
    for row in f_csv:
        print( row )

#using namedtuple !
from collections import namedtuple
with open('stocks.csv') as f:
    f_csv = csv.reader(f)
    headings = next(f_csv)
    Row = namedtuple('Row', headings)
    for r in f_csv:
        row = Row(*r)
        print(row)


headers = ['Symbol','Price','Date','Time','Change','Volume']
rows = [('AA', 39.48, '6/11/2007', '9:36am', -0.18, 181800),
('AIG', 71.38, '6/11/2007', '9:36am', -0.15, 195500),
('AXP', 62.58, '6/11/2007', '9:36am', -0.46, 935000)]
with open('stocks2.csv','w', newline='') as f:#empty newline
    f_csv = csv.writer(f)
    f_csv.writerow(headers)
    f_csv.writerows(rows)#have empty line ,reading use csv have error

with open('stocks2.csv') as f:
    f_csv = csv.reader(f)
    headings = [re.sub('[^a-zA-Z_]','_',h ) for h in next(f_csv)]
    Row = namedtuple('Row', headings)
    for r in f_csv:
        row = Row(*r)
        print(row)

col_types = [str, float, str, str, float, int ]

with open('stocks2.csv') as f:
    f_csv = csv.reader(f)
    headers = next( f_csv )
    for r in f_csv:
        row = tuple( convert( value ) for convert, value in zip( col_types, row))
        print(row)


print('Reading as dicts with type conversion')
field_types = [ ('Price', float),
('Change', float),
('Volume', int) ]

with open('stocks2.csv') as f:
    for row in csv.DictReader(f):
        row.update((key, conversion(row[key])) for key, conversion in field_types)
        print(row)