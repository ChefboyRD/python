numerator = int(input('Numerator: '))
denominator = int(input('Denominator: '))

if denominator == 0:
	print('Error - cannot divide by zero.')
else:
	answer = numerator / denominator
	print(answer)
