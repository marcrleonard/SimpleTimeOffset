SimpleTimeOffset
================

This library provides a very simple way to add hour offsets to a given time.

Why?
----
While doing an iot project with micro python, I found that an internet connected device will get the correct time, but micropython would not give you the ability to add a timezone. So if you know (or figure out) the proper hourly offset, you can use this library to get the correct time.
It has no dependencies (except the `new_time` method, so you can easily use in micro python.
This does not do any other 'fancy' calculations like daylight savings time.

Example...
----------

```
import SimpleTimeOffset

current_time = (2017, 10, 27, 10, 39, 23, 4, 300)

time_set = SimpleTimeOffset(start_time=current_time)

offset_hours = 96
time_set.offset_hours(offset_hours)

print('Offset   {}'.format(offset_hours))
print('Original {}:{:02d}:{:02d}'.format(time_set.hour_current, time_set.minute_current, time_set.second_current))
print('New      {}:{:02d}:{:02d}'.format(time_set.hour_new, time_set.minute_current, time_set.second_current))
print('Offset   {} Days, {} Hours'.format(time_set.day_offset, time_set.hour_remainder))

print(time_set)
print(time_set.new_time())
```
This yields...

```
Offset   96
Original 10:39:23
New      10:39:23
Offset   4 Days, 0 Hours
10:39
2017-10-31 10:39:23.000004
```

Todo:
-----
Add other `start_time` inputs. Right now, it only supports a tuple as shown above (this is what micro python uses as a time output - not a time object).
Add negative times
Add month offset (if hours > 24*31 or whatever the month value is.)
