red = int(input('Enter the red: '))
green = int(input('Enter the green: '))
blue = int(input('Enter the blue: '))

text = ''

print('')

if red < 0 or red > 255:
	text += 'Red number is incorrect'

if green < 0 or green > 255:
	text += '\nGreen number is incorrect'

if blue < 0 or blue > 255:
	text += '\nBlue number is incorrect'

print(text)
