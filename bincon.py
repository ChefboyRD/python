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

print ('{} {} {}'.format(d, q, r))

n = r

# div 64

d = int(d / 2)
q = int(n / d)
binArray.append(q)
r = int(n % d)

print ('{} {} {}'.format(d, q, r))

n = r

# div 32

d = int(d / 2)
q = int(n / d)
binArray.append(q)
r = int(n % d)

print ('{} {} {}'.format(d, q, r))

n = r

# div 16

d = int(d / 2)
q = int(n / d)
binArray.append(q)
r = int(n % d)

print ('{} {} {}'.format(d, q, r))

n = r

# div 8

d = int(d / 2)
q = int(n / d)
binArray.append(q)
r = int(n % d)

print ('{} {} {}'.format(d, q, r))

n = r

# div 4

d = int(d / 2)
q = int(n / d)
binArray.append(q)
r = int(n % d)

print ('{} {} {}'.format(d, q, r))

n = r

# div 2

d = int(d / 2)
q = int(n / d)
binArray.append(q)
r = int(n % d)

print ('{} {} {}'.format(d, q, r))

n = r

# div 1

d = int(d / 2)
q = int(n / d)
binArray.append(q)
r = int(n % d)

print ('{} {} {}'.format(d, q, r))

n = r

for x in binArray:
	print (x, end = '')

print()
