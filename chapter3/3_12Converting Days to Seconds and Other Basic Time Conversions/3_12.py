from datetime import  timedelta

a = timedelta( days=2, hours=6)
b = timedelta( hours= 4.5 )
c = a + b
print( c.days, c.seconds, c.seconds/3600, c.total_seconds()/3600 )
b = timedelta(hours=-4.5)
print( a + b )

from datetime import  datetime
a = datetime(2012,9,23)
print( a + timedelta(days=10))
b = datetime( 2012,12,21)
d = b - a
print( d.days )
now = datetime.today()
print( now )
print( now + timedelta( minutes=10))

from dateutil.relativedelta import relativedelta

a = datetime.today()
print( a - relativedelta(months=+1))
print( a + relativedelta( months=+4) )
b = datetime(2021,1,1)
d = b - a
print( d )
print( relativedelta(b,a ))
