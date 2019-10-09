a = int(input('Enter side A: '))
b = int(input('Enter side B: '))
c = int(input('Enter side C: '))
d = int(input('Enter side D: '))
e = int(input('Enter side E: '))

print('Room Area: ', str((a*b) + ((d-b-e)*(a-c)) + (e*(a-c))/2))
