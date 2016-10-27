#Corey Henry & Samuel Howle              #Date Assigned: 01Oct2014
#                             #
#Course CSE 1284 Sec 02       #Date Due: 07Oct2014
#File name: lab5.py
#
#Program description - make a simple dice game according to snakes and ladders
#going to 100, incorparate 2 players, and incorparate snakes and ladders.

#import the random for dice rolling
import random
#set values for beginning location
SA = 0
SB = 0
#START ROLLING LOOP
while SA < 100 and SB < 100:
    roll = random.randint(1,6)
    A = roll
    SA += A
    # if statements for snakes and ladders
    if SA == 99:
        SA = 6
    elif SA == 88:
        SA = 67
    elif SA == 71:
        SA = 29
    elif SA == 55:
        SA = 13
    elif SA == 24:
        SA = 1
    elif SA == 42:
        SA = 81
    elif SA == 66:
        SA = 87
    elif SA == 8:
        SA = 31
    elif SA == 15:
        SA = 97
#Player A's turn loop
    while A == 1 or A == 6:
        print('A = ', roll,'SA = ', SA,'it is turn of player A')
#repeat player A's turn
        roll = random.randint(1,6)
        A = roll
        SA += roll
        # if statements for snakes and ladders
        if SA == 99:
            SA = 6
        elif SA == 88:
            SA = 67
        elif SA == 71:
            SA = 29
        elif SA == 55:
            SA = 13
        elif SA == 24:
            SA = 1
        elif SA == 42:
            SA = 81
        elif SA == 66:
            SA = 87
        elif SA == 8:
            SA = 31
        elif SA == 15:
            SA = 97
#exec function for snakes and ladder for player A
        input('Hit enter to throw the dice')
    print('A = ', roll, 'SA = ', SA, 'it is turn of player B')
    input('Hit enter to throw the dice')
#Player B's turn loop
    roll = random.randint(1,6)
    B = roll
    SB += B
    # if statements for snakes and ladders
    if SB == 99:
        SB = 6
    elif SB == 88:
        SB = 67
    elif SB == 71:
        SB = 29
    elif SB == 55:
        SB = 13
    elif SB == 24:
        SB = 1
    elif SB == 42:
        SB = 81
    elif SB == 66:
        SB = 87
    elif SB == 8:
        SB = 31
    elif SB == 15:
        SB = 97
    while B == 1 or B == 6:
        print('B = ', roll,'SB = ', SB,'it is turn of player B')
#Repeat player B's turn
        roll = random.randint(1,6)
        B = roll
        SB += roll
        # if statements for snakes and ladders
        if SB == 99:
            SB = 6
        elif SB == 88:
            SB = 67
        elif SB == 71:
            SB = 29
        elif SB == 55:
            SB = 13
        elif SB == 24:
            SB = 1
        elif SB == 42:
            SB = 81
        elif SB == 66:
            SB = 87
        elif SB == 8:
            SB = 31
        elif SB == 15:
            SB = 97
#excute function for snakes and laders for player B
        input('Hit enter to throw the dice')
    print('B = ', roll,'SB = ', SB,'it is turn of player A')
    input('Hit enter to throw the dice')
    
    
   
# when SA >= 100 give player B another turn before declaring winner
if SA >= 100:
    roll = random.randint(1,6)
    B = roll
    SB += B
    #if statements for snakes and ladders
    if SB == 99:
        SB = 6
    elif SB == 88:
        SB = 67
    elif SB == 71:
        SB = 29
    elif SB == 55:
        SB = 13
    elif SB == 24:
        SB = 1
    elif SB == 42:
        SB = 81
    elif SB == 66:
        SB = 87
    elif SB == 8:
        SB = 31
    elif SB == 15:
        SB = 97
    # loop for rerolling
    while B == 1 or B == 6:
        input('Hit enter to throw the dice')
        print('B = ', roll,'SB = ', SB,'it is turn of player A')
        roll == random.randint(1,6)
        B = roll
        SB += roll
        # if statements for snakes and ladders
        if SB == 99:
            SB = 6
        elif SB == 88:
            SB = 67
        elif SB == 71:
            SB = 29
        elif SB == 55:
            SB = 13
        elif SB == 24:
            SB = 1
        elif SB == 42:
            SB = 81
        elif SB == 66:
            SB = 87
        elif SB == 8:
            SB = 31
        elif SB == 15:
            SB = 97
        input('Hit enter to throw the dice')
        print('B = ', roll,'SB = ', SB,'it is turn of player A')
# if at the end of the loop if B doesnt = 100 or more than player A wins
    if SB < 100:
        print(' Player A has won')
        

# if SB gets to 100 first then they win        
if SB >= 100:
    print('player B has won')

    
