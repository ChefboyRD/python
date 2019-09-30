hour = int(input('Enter the hour: '))
minute = int(input('Enter the minute: '))

minute += 15

#ft += int(it / 12)

#it = int(it % 12)

while minute > 59:
	hour += int(minute/60)
	minute %= 60
	
if hour > 12:
	hour -= 12

print('Hours: {}\nMinutes: {}'.format(hour, minute))
