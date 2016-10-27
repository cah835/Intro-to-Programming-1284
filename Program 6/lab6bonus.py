#Corey Henry & Samuel Howle & Michael Bishop             #Date Assigned: 015Oct2014
#                                                        #
#Course CSE 1284 Sec 02                                  #Date Due: 22Oct2014
#File name: lab6.py
#
#Program description- Create a Atm prompt user screen

#global variable for checking and savings ammounts

# inquiry function
def inquiry(checking,savings):
    print('Checking account balance: ', checking)
    print('Savings account balance: ', savings)
    stop(checking,savings)
#deposit to checking function
def deposit_check(checking,savings):
    cash = float(input('Ammount to be deposited: '))
    checking += cash
    print('Transaction Complete')
    inquiry(checking,savings)
    return (checking)
    stop(checking,savings)

#deposit to savings function
def deposit_save(checking,savings):
    cash = float(input('Ammount to be deposited: '))
    savings += cash
    print('Transaction Complete')
    inquiry(checking, savings)
    stop(checking,savings)
    return savings
#Withdrawal from checking
def withdrawal_c(checking,savings):
    cash = float(input('Amount to be withdrawn: '))
    while cash > checking:
        print('Your account has insufficient funds.')
        print('Transaction cannot be completed.')
        cash = float(input('Amount to be withdrawn.'))
    print('Transaction is complete')
    checking -= cash
    inquiry(checking,savings)
    stop(checking,savings)
    return checking
#Withdrawal from savings
def withdrawal_s(checking,savings):
    cash = float(input('Amount to be withdrawn: '))
    while cash > savings:
        print('Your account has insufficient funds.')
        print('Transaction cannot be completed.')
        cash = float(input('Amount to be withdrawn.'))
    print('Transaction is complete')
    savings -= cash
    inquiry(checking,savings)
    stop(checking,savings)
    return savings
#quit function
def stop(checking,savings):
    cont = input('Would you like to make another transaction? (Y/N): ')
    if cont == ('n'):
        print('\n')
        end_prog(checking,savings)
    elif cont == ('y'):
        options(checking,savings)
    return
#create end fuction
def end_prog(checking,savings):
    print('Checking account balance: ', checking)
    print('Savings account balance: ', savings)
    print('Thank you, Come again.')
#options function
def options(checking,savings):
    print('1. Account Inquiry')
    print('2. Deposit to Checking')
    print('3. Deposit to Savings')
    print('4. Withdraw from Checking')
    print('5. Withdraw from Savings')
    print('6. Quit')
    print('\n')
    option = int(input('Please select an option: '))
#create validation loop
    while option > 6 or option < 1:
        print('Error: please select a number 1 through 6')
        option = int(input('Please select an option: '))
    if option == 1:
        inquiry(checking,savings)
    elif option == 2:
        checking = deposit_check(checking,savings)
    elif option == 3:
        savings = deposit_save(checking,savings)
    elif option == 4:
        checking =withdrawal_c(checking,savings)
    elif option == 5:
        savings = withdrawal_s(checking,savings)
    elif option == 6:
        end_prog(checking,savings)                       
# create main function
def main():
    user2 = ('Diddy Kong')
    cont = ('y')
    user1 = ('Lion King')
    
    while cont == ('y'):
        pin_number = int(input('Welcome! Please enter your 4 digit PIN: '))
        if pin_number == 1234:
            user = user2
            checking = 1000
            savings = 23000
        elif pin_number == 4321:
            user = user1
            checking = 1500
            savings = 37856
        else:
            print('Sorry! Please try again.')
            pin_number = int(input('Welcome! Please enter your 4 digit PIN: '))
        print('Welcome back, ', user)
        options(checking,savings)
#call main function
main()

    
    

    
    
