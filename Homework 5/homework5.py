#Corey Henry                  #Date Assigned: 15Oct2014
#                             #
#Course CSE 1284 Sec 02       #Date Due: 20Oct2014
#File name: homework#5.py
#
#Program descirption: Takes the 12 intergers and uses the math provided to
#determine if the ISBN is correct or not.

# get intergers from user
a = int(input("please choose a number to represent A "))
b = int(input('please choose a number to represent B '))
n = int(input('please chooose a number to represent N '))

#addition function
def add_fn(a,b):
    a_list = [1] * a
    b_list = [1] * b
    c_list = a_list + b_list
    print(c_list)
    total = len(c_list)
    print(total)

       

#subtration function
def sub_fn(a,b):
    a_list = [1] * a
    b_list = [-1] * b
    c_list = a_list + b_list
    print(c_list)
    total = len(a_list)
    total2 = len(b_list)
    print(total - total2)


#def multipicaiton
def mult_fn(a,b):
    a_list = [a] * b
    print(a_list)
    total = sum(a_list)
    print(total)


#def expo
def pow_fn(a,b):
    a_list = [a]*a
    total2 = 0
    for each_one in range(b):
        for each_one in range(b):
            total2 += len(a_list)
    print(total2)


    
#def main function to call all functions   
def main(a,b):
    add_fn(a,b)
    print('\n')
    sub_fn(a,b)
    print('\n')
    mult_fn(a,b)
    print('\n')
    pow_fn(a,b)
#
#call main function
main(a,b)

        
 



