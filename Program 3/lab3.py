#Corey Henry                  #Date Assigned: 17SEP2014
#                             #
#Course CSE 1284 Sec 02       #Date Due: 17Sep2014
#File name: lab3.py
#
#Program descirption: Takes the 12 intergers and uses the math provided to
#determine if the ISBN is correct or not.



print('Enter the ISBN one digit at a time')
print('\n')
#find out the 12 intergers and the check digit
D1 = int(input('Enter digit: '))
D2 = int(input('Enter digit: '))
D3 = int(input('Enter digit: '))
D4 = int(input('Enter digit: '))
D5 = int(input('Enter digit: '))
D6 = int(input('Enter digit: '))
D7 = int(input('Enter digit: '))
D8 = int(input('Enter digit: '))
D9 = int(input('Enter digit: '))
D10 = int(input('Enter digit: '))
D11 = int(input('Enter digit: '))
D12 = int(input('Enter digit: '))
C1 = int(input('Check digit: '))
#find out the total
total = (D1 + (D2*3) + D3 + (D4*3) + D5 + (D6*3) + D7 + (D8*3) + D9 + (D10*3) + D11 + (D12*3))
#find the remainder
REM = total % 10
# find the final number
math = 10- REM
 
print('The check didgit is', C1)
# if statement for when the check digit is 0 so it doesnt show 10
if math == 10:
    print('The calculated check digit is: 0')
else:
 print('The calculated check digit is: ', math)

