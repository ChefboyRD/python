x = []

y = 0

print('Enter 3 float(decimal number): ')

for i in range(0, 3):
	x.append(float(input()))
	y += x[i]

print(y)
