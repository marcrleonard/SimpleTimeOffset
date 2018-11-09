from SimpleTimeOffset import SimpleTimeOffset

# utime.localtime(ntptime.time()) output == (2017, 10, 27, 12, 39, 23, 4, 300)
current_time = (2017, 12, 27, 13, 39, 23, 4, 300)

time_set = SimpleTimeOffset(start_time=current_time, millitary=True)
offset_hours = 3
time_set.offset_hours(offset_hours)

print('Offset   {}'.format(offset_hours))
print('Original {}:{:02d}:{:02d}'.format(time_set.hour_current, time_set.minute_current, time_set.second_current))
print('New      {}:{:02d}:{:02d}'.format(time_set.hour_new, time_set.minute_current, time_set.second_current))
print('Offset   {} Days, {} Hours'.format(time_set.day_offset, time_set.hour_remainder))

# print(time_set)
# print(time_set.new_time())


digits_str = '{}{:02d}'.format(time_set.hour_new, time_set.minute_current)
digits = [int(n) for n in digits_str]
print(digits)