#import datetime
#now = datetime.datetime.now()
#print now.year, now.month, now.day, now.hour, now.minute, now.second
import datetime
now = datetime.datetime.now()
print 86400 - (now.hour * 3600) - (now.minute * 60) - now.second
