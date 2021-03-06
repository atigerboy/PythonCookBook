from datetime import  datetime,timedelta

import pytz
from pytz import  timezone


d = datetime(2012, 12, 21, 9, 30, 0)
# Localize the date for Chicago
central = timezone('US/Central')
loc_d = central.localize(d)
print( loc_d )

# Convert to Bangalore time
bang_d = loc_d.astimezone(timezone('Asia/Kolkata'))
print(bang_d)

d = datetime(2013, 3, 10, 1, 45)
loc_d = central.localize(d)
print(loc_d)
later = loc_d + timedelta(minutes=30)
print(later)

later = central.normalize(loc_d + timedelta(minutes=30))
print(later)

utc_d = loc_d.astimezone( pytz.utc )
later_utc = utc_d + timedelta(minutes=30)

print(later_utc.astimezone(central))

print( '\n'.join(pytz.common_timezones ))
