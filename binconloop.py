# 191 = 1011 1111

# q = quotient
# d = devisor
# r = remainder
# n = integer input

binArray = [];

correctInput = False

# div 128

while (correctInput == False):
	n = int(input('Integer (< 256): '))
	
	if (n > -1 and n < 256):
		correctInput = True
	else:
		correctInput = False

d = 128
q = int(n / d)
binArray.append(q)
r = int(n % d)

#print ('{} {} {}'.format(d, q, r))

for x in range(7):
	n = r
	d = int(d / 2)
	q = int(n / d)
	binArray.append(q)
	r = int(n % d)

	#print ('{} {} {}'.format(d, q, r))

	n = r
	
for x in binArray:
	print (x, end = '')

print()
