from datetime import datetime
text = '2012-09-20'
y = datetime.strptime( text, '%Y-%m-%d')#%Y 4digit year %m 2 digit month
z = datetime.now()

print( y, z, z-y)
#strong recommand
nice_z = datetime.strftime(z, '%A %B %d %Y')
print( nice_z )
#try 'parse YYYY-MM-DD' format
def parse_ymd(s:str):
    year_s, mon_s, day_s = s.split('-')
    return datetime(int(year_s), int(mon_s), int(day_s) )

print( parse_ymd( text ))