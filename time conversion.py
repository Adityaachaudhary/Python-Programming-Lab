'''Given a time in -hour AM/PM format, convert it to military (24-hour) time.
Example

s = '12:01:00PM'
Return '12:01:00'.

s = '12:01:00AM'
Return '00:01:00'.'''

s = input()
t = s.split(":")

