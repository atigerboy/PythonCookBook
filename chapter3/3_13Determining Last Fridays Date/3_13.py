from datetime import datetime,timedelta

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday','Friday', 'Saturday', 'Sunday']

def get_previous_byday( dayname, start_date = None ):
    if start_date == None:
        start_date = datetime.today()
    day_num = start_date.weekday()
    day_num_target = weekdays.index( dayname )
    days_ago = (7 + day_num - day_num_target) % 7
    if days_ago == 0:
        days_ago = 7
    target_date = start_date - timedelta(days=days_ago)
    return target_date

print( datetime.today() )
print( get_previous_byday( weekdays[0] ))
print( get_previous_byday( weekdays[6] ))
print( get_previous_byday(weekdays[6], datetime(2021,8,5)))

from dateutil.relativedelta import relativedelta
from dateutil.rrule import  *

d = datetime.now()
print( d )

#Next Friday
print(d + relativedelta(weekday=FR))

# Last Friday
print(d + relativedelta(weekday=FR(-1)))