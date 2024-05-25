#09_Modules - Time Module
'''
Python 3.11.8 (tags/v3.11.8:db85d51, Feb  6 2024, 22:03:32) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import time as t
t.localtime()
time.struct_time(tm_year=2024, tm_mon=2, tm_mday=12, tm_hour=23, tm_min=55, tm_sec=0, tm_wday=0, tm_yday=43, tm_isdst=0)
time_now = t.localtime()
print("Transaction completed at", str(time_now.tm_hour) + "h" + str(time_now.tm_min) + "m")
Transaction completed at 23h56m
t.time()
1707793076.2208827
t.time()
1707793081.7382753
t.time()
1707793086.0143652
t.time()
1707793097.8118463
time_now = t.time()
delivery_time = time_now + (86400 * 7)
t.localtime(delivery_time)
time.struct_time(tm_year=2024, tm_mon=2, tm_mday=19, tm_hour=23, tm_min=59, tm_sec=20, tm_wday=0, tm_yday=50, tm_isdst=0)
t.sleep(5)
t.countdown(5)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    t.countdown(5)
AttributeError: module 'time' has no attribute 'countdown'
print("With time.sleep you can make the program wait 5 seconds, using this for a countdown or simplest time operations")
With time.sleep you can make the program wait 5 seconds, using this for a countdown or simplest time operations
'''
