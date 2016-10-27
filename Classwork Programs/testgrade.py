count = 0
total = 0

while count < 3:
    test = float(input('Enter the test grade: '))
    while test < 0 or test > 110:
        print('ERROR: invalid test grade.')
        test= float(input('Enter the test grade: '))
    total += test
    count += 1

average = total / 3

print('Average test grade: ', average)
