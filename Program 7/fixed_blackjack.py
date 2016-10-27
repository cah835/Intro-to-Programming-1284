#Corey Henry                  #Date Assigned: 07Oct2014
#                             #
#Course CSE 1284 Sec 02       #Date Due: 14Oct2014
#File name: fixed_blackjack.py
#
#Program description - plays black jack
#





import random


def main():
        #start game automatically
        play_again = 'y'
        if play_again == 'y':
                #get random card values for the player and computer
                user1 = random_card()
                user2 = random_card()
                user3 = -1
                computer1 = random_card()
                computer2 = random_card()
                computer3 = -1
                print("User:", get_card_value(user1), "", get_card_value(user2), end='')

                #if statement if they user wants another card and if computer gets one
                if user3 != -1:
                        print("User:",get_card_value(user3), end='')
                if computer3 != -1:
                        print("", get_card_value(computer3), end='')
                print("\nComputer:", get_card_value(computer1), "", get_card_value(computer2), end='')
                # print new line
                print("\n")
                #tally up the scores for the user and computer
                userscore = second_hand(user1, user2, user3)
                computerscore = second_hand(computer1, computer2, computer3)
                #prompt user for another card
                user3 = another_card()
                userscore = second_hand(user1, user2, user3)
                #if user got another card then excute to print it
                if user3 != -1:
                        print("User:",get_card_value(user3), end='')
                #if the user is winning and under or equal to 21 computer gets another card
                if(userscore > computerscore and userscore <= 21):
                        computer3 = random_card()
                print("User:", get_card_value(user1), "", get_card_value(user2), end='')


                print("\nComputer:", get_card_value(computer1), "", get_card_value(computer2), end='')

                if computer3 != -1:
                        print("", get_card_value(computer3), end='')
                        print("\n")
                computerscore = second_hand(computer1, computer2, computer3)
                print('\n')
                print("User score: ", userscore)
                print("Computer score: ", computerscore)
                #if the user goes over 21 print he busts
                if userscore > 21:
                        print("Busted!")
                #if the scores match it's a tie
                elif userscore == computerscore:
                        print("It's a tie")
                #if computers score is higher than you loose
                elif computerscore <= 21 and computerscore > userscore:
                        print("Sorry. You lost!")
                #if computer score is lower than you win
                elif userscore <= 21 and userscore > computerscore:
                        print("Congratulations! You won.")
               #ask if they want to play again 
                play_again = input("Do you want to play again? (y/n)")
                print('\n')
                # if they dont enter y or N
                while play_again != 'y' and play_again !='n':
                        print("Please enter only a 'y' or 'n'")
                        play_again = input("Do you want to play again?")
                if play_again == 'y':
                        main()
        

#get a random card
def random_card():
	return random.randint(0,51)
#determine the value of the card	
def get_card_value(card):
        #change value for face cards
	faceValue = int(card / 4) + 1
	suit = card % 4
	if faceValue == 0:
		faceValue = ""
	elif faceValue == 1:
		faceValue = 'A'
	elif faceValue == 11:
		faceValue = 'J'
	elif faceValue == 12:
		faceValue = 'Q'
	elif faceValue == 13:
		faceValue = 'K'
	else:
		faceValue = str(faceValue)
	#determine the suit of the card
	if suit == 0:
		suit = " Clubs"
	elif suit == 1:
		suit = " Diamonds"
	elif suit == 2:
		suit = " Hearts"
	elif suit == 3:
		suit = " Spades"
	else:
		suit = ""
		print("Error! Bad suit")
	return (faceValue, suit)



def second_hand(card1, card2, card3):
	score = 0
	faceValue1 = int(card1 / 4) + 1
	faceValue2 = int(card2 / 4) + 1
	faceValue3 = 0
	if card3 != -1:
		faceValue3 = int(card3 / 4) + 1
	if faceValue1 == 0:
		score1 = 0
	elif faceValue1 == 1:
		score1 = 11
	elif faceValue1 == 11 or faceValue1 == 12 or faceValue1 == 13:
		score1 = 10
	else:
		score1 = faceValue1	
	if faceValue2 == 0:
		score2 = 0
	elif faceValue2 == 1:
		score2 = 11
	elif faceValue2 == 11 or faceValue2 == 12 or faceValue2 == 13:
		score2 = 10
	else:
		score2 = faceValue2
	if faceValue3 == 0:
		score3 = 0
	elif faceValue3 == 1:
		score3 = 11
	elif faceValue3 == 11 or faceValue3 == 12 or faceValue3 == 13:
		score3 = 10
	else:
		score3 = faceValue3
	score = score1 + score2 + score3
	return score

def another_card():
        answer = input("Would you like one more card? (y/n) ")
        while answer != 'y' and answer != 'n':
                print("Please enter 'y' or 'n'")
                answer = input("Would you like one more card? (y/n) ")
        if answer == 'y':
                return random_card()
        else:
                return -1
        
	
main()
