grade = int(input('What grade are you in? '))

text = ''

if grade == 9:
	text = 'Freshman'
elif grade == 10:
	text = 'Sophomore'
elif grade == 11:
	text = 'Junior'
elif grade == 12:
	text = 'Senior'
else:
	text = 'Not in High School'

print(text)
