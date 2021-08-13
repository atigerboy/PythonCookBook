from datetime import  datetime, date, timedelta
import calendar

def get_month_range( start_date = None ):
    if start_date == None:
        start_date = datetime.today().replace(day=1) #the 1st day of this month
    _,days_in_month = calendar.monthrange(start_date.year, start_date.month )#get days number
    end_date = start_date+timedelta( days= days_in_month)
    return (start_date, end_date)

a_day = timedelta(days=1)
first_day, last_day = get_month_range()
while first_day < last_day:
    print( first_day )
    first_day += a_day

def date_range( start, stop, step ):
    while start < stop:
        yield  start
        start += step

for d in date_range( *get_month_range(), timedelta(hours=6) ):
    print( d )
