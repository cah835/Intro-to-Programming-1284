# Corey Henry                   #Date Assigned = 3Oct4
#                               #
#Course CSE 1284 Section :2     #Date Due = 10Oct14
#
#File name: diamonds.py
#
#program description: make a program that prints a diamond with the right ammount
#of stars thats user inputs

#Get the height of the diamond
height = int(input('What is the height of the diamond? '))
#input validation
while (height == 0) or (height %2 == 0):
    print('ERROR: the height must be an odd number greater than 0')
    height = int(input('what is the height of the diamond? '))
#print the validated height
print('The validated height of the diamond is: ', height)

#get half the diamond top by taking the height, getting half of it plus 1
top_half = height // 2 + 1
spaces = top_half
#for loop to print the diamond and space
for diamonds in range(top_half):
    for spaces in range (spaces+1):
        print(' ', end = '')
        spaces -=1
    for columns in range(diamonds+1):
        print('*',end =' ')
    print()
bottom_half = height //2
spaces = 2
#for loop to print the diamond and space
for bottom_half in range(bottom_half,0,-1):
    for spaces in range (spaces+1):
        print(' ', end = '')
        spaces +=1
    for columns in reversed(range(bottom_half,0,-1)):
        print('*',end =' ')
    print()
