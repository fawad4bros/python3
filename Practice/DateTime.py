#What is Tick?
import time
ticks = time.time()
print("Number of ticks since 12:00am, January 1, 1970:", ticks)
# OutPut Number of ticks since 12:00am, January 1, 1970: 1615641366.0096605
#Date arithmetic is easy to do with ticks

# Many of Python's time functions handle time as a tuple of 9 numbers, as shown below −

#What is TimeTuple?
#An n-tuple is a sequence (or ordered list) of n elements, where n is a non-negative integer.

# Index	Field	        Values
# 0	4-digit year	    2008
# 1	Month	            1 to 12
# 2	Day	                1 to 31
# 3	Hour	            0 to 23
# 4	Minute	            0 to 59
# 5	Second	            0 to 61 (60 or 61 are leap-seconds)
# 6	Day of Week	        0 to 6 (0 is Monday)
# 7	Day of year	        1 to 366 (Julian day)
# 8	Daylight savings	-1, 0, 1, -1 means library determines DST

# The above tuple is equivalent to struct_time structure. This structure has following attributes −

# Index	Attributes	Values
# 0	    tm_year	    2008
# 1	    tm_mon	    1 to 12
# 2	    tm_mday	    1 to 31
# 3	    tm_hour	    0 to 23
# 4	    tm_min	    0 to 59
# 5	    tm_sec	    0 to 61 (60 or 61 are leap-seconds)
# 6	    tm_wday	    0 to 6 (0 is Monday)
# 7	    tm_yday	    1 to 366 (Julian day)
# 8	    tm_isdst    -1, 0, 1, -1 means library determines DST

# Getting current time !
# To translate a time instant from a seconds since the epoch floating-point value into a time-tuple, 
# pass the floating-point value to a function (e.g., localtime) that returns a time-tuple with all nine items valid.

localtime = time.localtime(time.time())
print ("Local current time :", localtime)

# Getting formatted time !
# You can format any time as per your requirement, but simple method to get time in readable format is asctime() −

localtime = time.asctime( time.localtime(time.time()) )
print ("Local current time :", localtime)

# UTC (Coordinated Universal Time)
# Daylight saving time (DST)
print ("time.altzone %d " % time.altzone)


# Getting calendar for a month !
# The calendar module gives a wide range of methods to play with yearly and monthly calendars. Here, we print a calendar for a given month ( Jan 2021 ) −

import calendar

cal = calendar.month(2021, 1)
print ("Here is the calendar:")
print (cal)