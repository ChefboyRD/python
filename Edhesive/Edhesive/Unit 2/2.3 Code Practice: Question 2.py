f1 = int(input('Enter the Feet for the first piece of fabric: '))
i1 = int(input('Enter the Inches for the first piece of fabric: '))

f2 = int(input('Enter the Feet for the second piece of fabric: '))
i2 = int(input('Enter the Inches for the second piece of fabric: '))

ft = f1 + f2
it = i1 + i2

ft += int(it / 12)

it = int(it % 12)

print('Feet: {} Inches: {}'.format(ft, it))
