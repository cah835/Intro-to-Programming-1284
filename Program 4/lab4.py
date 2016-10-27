#Corey Henry                  #Date Assigned: 24SEP2014
#                             #
#Course CSE 1284 Sec 02       #Date Due: 24Sep2014
#File name: lab4.py
#
#Program description - 2 player game of match! to see who wins
#
# give cards variable names
card1 = ("('1'")
card2 = ("'2'")
card3 = ("'3'")
card4 = ("'4'")
card5 = ("'5'")
card6 = ("'6'")
card7 = ("'7'")
card8 = ("'8')")
#display cards
print(card1,card2,card3,card4,card5,card6,card7,card8)
#Assign card values
card_1 = ("'Peach'")
card_2 = ("'Mario'")
card_3 = ("'Yoshi'")
card_4 = ("'Peach'")
card_5 = ("'Yoshi'")
card_6 = ("'Mario'")
card_7 = ("'Bowser'")
card_8 = ("'Bowser'")
#Starting score
player_1_points = 0
player_2_points = 0
# player 1 flips a card
attempt_1 = int(input('Player 1, Flip a card: '))
if attempt_1 == 1:
    print('Card 1 is',card_1)
elif attempt_1 == 2:
    print('Card 2 is',card_2)
elif attempt_1 == 3:
    print('Card 3 is',card_3)
elif attempt_1 == 4:
    print('Card 4 is',card_4)
elif attempt_1 == 5:
    print('Card 5 is',card_5)
elif attempt_1 == 6:
    print('Card 6 is',card_6)
elif attempt_1 == 7:
    print('Card 7 is',card_7)
elif attempt_1 == 8:
    print('Card 8 is',card_8)
#
#    
# player 1 flips another card
#
#
attempt_2 = int(input('Player 1, Flip another card: '))
if attempt_2 == 1:
    print('Card 1 is',card_1)
elif attempt_2 == 2:
    print('Card 2 is',card_2)
elif attempt_2 == 3:
    print('Card 3 is',card_3)
elif attempt_2 == 4:
    print('Card 4 is',card_4)
elif attempt_2 == 5:
    print('Card 5 is',card_5)
elif attempt_2 == 6:
    print('Card 6 is',card_6)
elif attempt_2 == 7:
    print('Card 7 is',card_7)
elif attempt_2 == 8:
    print('Card 8 is',card_8)
# change player 1 points and card names if correct
if (attempt_1 == 1 or attempt_1 == 4)  and (attempt_2 == 4 or attempt_2 ==1):
    card1 = ("'Peach'")
    card4 = ("'Peach'")
    print('They are a Match!')
    player_1_points = 1
elif (attempt_1 == 2 or attempt_1 == 6) and (attempt_2 == 6 or attempt_2 == 2):
    card2 = ("'Mario'")
    card6 = ("'Mario'")
    print('They are a Match!')
    player_1_points = 1
elif (attempt_1 == 3 or attempt_1 ==  5) and (attempt_2 == 5 or attempt_2 == 3):
    card3 = ("'Yoshi'")
    card5 = ("'Yoshi'")
    print('They are a Match!')
    player_1_points = 1
elif (attempt_1 == 7 or attempt_1 == 8) and (attempt_2 == 8 or attempt_2 == 7):
    card7 = ("'Bowser'")
    card8 = ("'Bowser'")
    print('They are a Match!')
    player_1_points = 1
#print new line
print('\n')
#
#
# display cards
print(card1,card2,card3,card4,card5,card6,card7,card8)
#
#player 2 picks a card
attempt_3 = int(input('Player 2 flip a card: '))
if attempt_3 == 1:
    print('Card 1 is',card_1)
elif attempt_3 == 2:
    print('Card 2 is',card_2)
elif attempt_3 == 3:
    print('Card 3 is',card_3)
elif attempt_3 == 4:
    print('Card 4 is',card_4)
elif attempt_3 == 5:
    print('Card 5 is',card_5)
elif attempt_3 == 6:
    print('Card 6 is',card_6)
elif attempt_3 == 7:
    print('Card 7 is',card_7)
elif attempt_3 == 8:
    print('Card 8 is',card_8)
#Player 2 flips another card
    #
    #
    #
attempt_4 = int(input('Player 2, Flip another a card: '))
if attempt_4 == 1:
    print('Card 1 is',card_1)
elif attempt_4 == 2:
    print('Card 2 is',card_2)
elif attempt_4 == 3:
    print('Card 3 is',card_3)
elif attempt_4 == 4:
    print('Card 4 is',card_4)
elif attempt_4 == 5:
    print('Card 5 is',card_5)
elif attempt_4 == 6:
    print('Card 6 is',card_6)
elif attempt_4 == 7:
    print('Card 7 is',card_7)
elif attempt_4 == 8:
    print('Card 8 is',card_8)
#change points and card name if a match
#
#
#
if (attempt_3 == 1 or attempt_3 == 4) and (attempt_4 == 4 or attempt_4 == 1):
    card1 = ("'Peach'")
    card4 = ("'Peach'")
    print('They are a Match!')
    player_2_points = 1
elif (attempt_3 == 2 or attempt_3 == 6) and (attempt_4 == 6 or attempt_4 == 2):
    card2 = ("'Mario'")
    card6 = ("'Mario'")
    print('They are a Match!')
    player_2_points = 1
elif (attempt_3 == 3 or attempt_3 == 5) and (attempt_4 == 5 or attempt_4 == 3):
    card3 = ("'Yoshi'")
    card5 = ('Yoshi')
    print('They are a Match!')
    player_2_points = 1
elif (attempt_3 == 7 or attempt_3 == 8) and (attempt_4 == 8 or attempt_4 == 7):
    card7 = ("'Bowser'")
    card8 = ("'Bowser'")
    print('They are a Match!')
    player_2_points = 1

#new line
print('\n')
#
#Start round 2
print('Here comes round 2!! Heres the score!')
print('player 1 =',player_1_points)
print('player 2 =',player_2_points)
#
#print new line
print('\n')
#print cards
print(card1,card2,card3,card4,card5,card6,card7,card8)
# player 1 flips a card
attempt_5 = int(input('Player 1, Flip a card: '))
if attempt_5 == 1:
    print('Card 1 is',card_1)
elif attempt_5 == 2:
    print('Card 2 is',card_2)
elif attempt_5 == 3:
    print('Card 3 is',card_3)
elif attempt_5 == 4:
    print('Card 4 is',card_4)
elif attempt_5 == 5:
    print('Card 5 is',card_5)
elif attempt_5 == 6:
    print('Card 6 is',card_6)
elif attempt_5 == 7:
    print('Card 7 is',card_7)
elif attempt_5 == 8:
    print('Card 8 is',card_8)
#
#    
# player 1 flips another card
#
#
attempt_6 = int(input('Player 1, Flip another card: '))
if attempt_6 == 1:
    print('Card 1 is',card_1)
elif attempt_6 == 2:
    print('Card 2 is',card_2)
elif attempt_6 == 3:
    print('Card 3 is',card_3)
elif attempt_6 == 4:
    print('Card 4 is',card_4)
elif attempt_6 == 5:
    print('Card 5 is',card_5)
elif attempt_6 == 6:
    print('Card 6 is',card_6)
elif attempt_6 == 7:
    print('Card 7 is',card_7)
elif attempt_6 == 8:
    print('Card 8 is',card_8)
# change player 1 points and card names if correct
if (attempt_5 == 1 or attempt_5 == 4) and (attempt_6 == 4 or attempt_6 == 1):
    card1 = ("'Peach'")
    card4 = ("'Peach'")
    print('They are a Match!')
    player_1_points = player_1_points + 1
elif (attempt_5 == 2 or attempt_5 == 6) and (attempt_6 == 6 or attempt_6 == 2):
    card2 = ("'Mario'")
    card6 = ("'Mario'")
    print('They are a Match!')
    player_1_points = player_1_points + 1
elif (attempt_5 == 3 or attempt_5 == 5) and (attempt_6 == 5 or attempt_6 == 3):
    card3 = ("'Yoshi'")
    card5 = ("'Yoshi'")
    print('They are a Match!')
    player_1_points = player_1_points + 1
elif (attempt_5 == 7 or attempt_5 == 8) and (attempt_6 == 8 or attempt_6 == 7):
    card7 = ("'Bowser'")
    card8 = ("'Bowser'")
    print('They are a Match!')
    player_1_points = player_1_points + 1
#print new line
print('\n')
#
# display cards
print(card1,card2,card3,card4,card5,card6,card7,card8)
#
#player 2 picks a card
attempt_7 = int(input('Player 2, Flip a card: '))
if attempt_7 == 1:
    print('Card 1 is',card_1)
elif attempt_7 == 2:
    print('Card 2 is',card_2)
elif attempt_7 == 3:
    print('Card 3 is',card_3)
elif attempt_7 == 4:
    print('Card 4 is',card_4)
elif attempt_7 == 5:
    print('Card 5 is',card_5)
elif attempt_7 == 6:
    print('Card 6 is',card_6)
elif attempt_7 == 7:
    print('Card 7 is',card_7)
elif attempt_7 == 8:
    print('Card 8 is',card_8)
#
#    
# player21 flips another card
#
#
attempt_8 = int(input('Player 2, Flip another card: '))
if attempt_8 == 1:
    print('Card 1 is',card_1)
elif attempt_8 == 2:
    print('Card 2 is',card_2)
elif attempt_8 == 3:
    print('Card 3 is',card_3)
elif attempt_8 == 4:
    print('Card 4 is',card_4)
elif attempt_8 == 5:
    print('Card 5 is',card_5)
elif attempt_8 == 6:
    print('Card 6 is',card_6)
elif attempt_8 == 7:
    print('Card 7 is',card_7)
elif attempt_8 == 8:
    print('Card 8 is',card_8)



# change player 2 points and card names if correct
if (attempt_7 == 1 or attempt_7 == 4) and (attempt_8 == 4 or attempt_8 == 1):
    card1 = ("'Peach'")
    card4 = ("'Peach'")
    print('They are a Match!')
    player_2_points = player_2_points + 1
elif (attempt_7 == 2 or attempt_7 == 6) and (attempt_8 == 6 or attempt_8 == 2):
    card2 = ("'Mario'")
    card6 = ("'Mario'")
    print('They are a Match!')
    player_2_points = player_2_points + 1
elif (attempt_7 == 3 or attempt_7 == 5) and (attempt_8 == 5 or attempt_8 == 3):
    card3 = ("'Yoshi'")
    card5 = ("'Yoshi'")
    print('They are a Match!')
    player_2_points = player_2_points + 1
elif (attempt_7 == 7 or attempt_7 == 8) and (attempt_8 == 8 or attempt_8 == 7):
    card7 = ("'Bowser'")
    card8 = ("'Bowser'")
    print('They are a Match!')
    player_2_points = player_2_points + 1


#new line    
print('\n')
#
#Start round 3
print('Here comes round 3!! Heres the score!')
print('player 1 =',player_1_points)
print('player 2 =',player_2_points)
#
#print new line
print('\n')
#print cards
print(card1,card2,card3,card4,card5,card6,card7,card8)
# player 1 flips a card
attempt_9 = int(input('Player 1, Flip a card: '))
if attempt_9 == 1:
    print('Card 1 is',card_1)
elif attempt_9 == 2:
    print('Card 2 is',card_2)
elif attempt_9 == 3:
    print('Card 3 is',card_3)
elif attempt_9 == 4:
    print('Card 4 is',card_4)
elif attempt_9 == 5:
    print('Card 5 is',card_5)
elif attempt_9 == 6:
    print('Card 6 is',card_6)
elif attempt_9 == 7:
    print('Card 7 is',card_7)
elif attempt_9 == 8:
    print('Card 8 is',card_8)
#
#    
# player 1 flips another card
#
#
attempt_11 = int(input('Player 1, Flip another card: '))
if attempt_11 == 1:
    print('Card 1 is',card_1)
elif attempt_11 == 2:
    print('Card 2 is',card_2)
elif attempt_11 == 3:
    print('Card 3 is',card_3)
elif attempt_11 == 4:
    print('Card 4 is',card_4)
elif attempt_11 == 5:
    print('Card 5 is',card_5)
elif attempt_11 == 6:
    print('Card 6 is',card_6)
elif attempt_11 == 7:
    print('Card 7 is',card_7)
elif attempt_11 == 8:
    print('Card 8 is',card_8)
# change player 1 points and card names if correct
if (attempt_9 == 1 or attempt_9 == 4) and (attempt_11 == 4 or attempt_11 == 1):
    card1 = ("'Peach'")
    card4 = ("'Peach'")
    print('They are a Match!')
    player_1_points = player_1_points + 1
elif (attempt_9 == 2 or attempt_9 == 6) and (attempt_11 == 6 or attempt_11 == 2):
    card2 = ("'Mario'")
    card6 = ("'Mario'")
    print('They are a Match!')
    player_1_points = player_1_points + 1
elif (attempt_9 == 3 or attempt_9 == 5) and (attempt_11 == 5 or attempt_11 == 3):
    card3 = ("'Yoshi'")
    card5 = ("'Yoshi'")
    print('They are a Match!')
    player_1_points = player_1_points + 1
elif (attempt_9 == 7 or attempt_9 == 8) and (attempt_11 == 8 or attempt_11 == 7):
    card7 = ("'Bowser'")
    card8 = ("'Bowser'")
    print('They are a Match!')
    player_1_points = player_1_points + 1
#print new line
print('\n')
#
# display cards
print(card1,card2,card3,card4,card5,card6,card7,card8)
#
#player 2 picks a card
attempt_12 = int(input('Player 2, Flip a card: '))
if attempt_12 == 1:
    print('Card 1 is',card_1)
elif attempt_12 == 2:
    print('Card 2 is',card_2)
elif attempt_12 == 3:
    print('Card 3 is',card_3)
elif attempt_12 == 4:
    print('Card 4 is',card_4)
elif attempt_12 == 5:
    print('Card 5 is',card_5)
elif attempt_12 == 6:
    print('Card 6 is',card_6)
elif attempt_12 == 7:
    print('Card 7 is',card_7)
elif attempt_12 == 8:
    print('Card 8 is',card_8)
#
#    
# player21 flips another card
#
#
attempt_13 = int(input('Player 2, Flip another card: '))
if attempt_13 == 1:
    print('Card 1 is',card_1)
elif attempt_13 == 2:
    print('Card 2 is',card_2)
elif attempt_13 == 3:
    print('Card 3 is',card_3)
elif attempt_13 == 4:
    print('Card 4 is',card_4)
elif attempt_13 == 5:
    print('Card 5 is',card_5)
elif attempt_13 == 6:
    print('Card 6 is',card_6)
elif attempt_13 == 7:
    print('Card 7 is',card_7)
elif attempt_13 == 8:
    print('Card 8 is',card_8)



# change player 2 points and card names if correct
if (attempt_12 == 1 or attempt_12 == 4) and (attempt_13 == 4 or attempt_13 == 1):
    card1 = ("'Peach'")
    card4 = ("'Peach'")
    print('They are a Match!')
    player_2_points = player_2_points + 1
elif (attempt_12 == 2 or attempt_12 == 6) and (attempt_13 == 6 or attempt_13 == 2):
    card2 = ("'Mario'")
    card6 = ("'Mario'")
    print('They are a Match!')
    player_2_points = player_2_points + 1
elif (attempt_12 == 3 or attempt_12 == 5) and (attempt_13 == 5 or attempt_13 == 3):
    card3 = ("'Yoshi'")
    card5 = ("'Yoshi'")
    print('They are a Match!')
    player_2_points = player_2_points + 1
elif (attempt_12 == 7 or attempt_12 == 8) and (attempt_13 == 8 or attempt_13 == 7):
    card7 = ("'Bowser'")
    card8 = ("'Bowser'")
    print('They are a Match!')
    player_2_points = player_2_points + 1


#new line    
print('\n')
#display final score
print('Heres the Final score!')
print('player 1 =',player_1_points)
print('player 2 =',player_2_points)
#
#print winning player
if player_1_points > player_2_points:
    print('Player 1 WINS!!!')
elif player_1_points < player_2_points:
    print('Player 2 WINS!!!')
elif player_1_points == player_2_points:
    print('You Tied!!!')

                    
