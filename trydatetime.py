import datetime
import pytz
import time
dt_now=datetime.datetime.now(pytz.UTC)
dt_mtn=datetime.datetime.today()
fmt='%A %d %b %Y %H:%M:%S %z'
D1=datetime.datetime.strptime(input("enter d1"),fmt)

D2=datetime.datetime.strptime(input("enter d2"),fmt)

difference=(D1-D2)

print(difference.total_seconds())


