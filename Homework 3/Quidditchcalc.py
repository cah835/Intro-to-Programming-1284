# Corey Henry                   #Date Assigned = 10Sep14
#                               #
#Course CSE 1284 Section :2     #Date Due = 17Sep14
#
#File name: Quidditchcal.py
#
#Program discription- the program should start off with an introduction, it will ask a series of question starting with the GS team and then the LS team,
#each teams variable begin with gs or ls depending on the order you put them in, it will then calaculate the scores for each them and display the score,
#whoever is eneterd under GS will automatically have a "1" under snitch and and whoever is ls will have a "0", then the it will calculate the goals per
#match
#
#
    #print intro
print("\t\t Welcome to CSE1284 Qudditch Calculator")
    #skip line
print('\n')
    #intro 2
print ("Enter the teams, score, and time to make it work. It's like Magic!")
#
#
    #skip line
print('\n')
    #find out winning team and store variable
gsteam = input ('Enter the name of the team that caught the golden snitch: ')
    # find out winning teams score and store as variable
gsscore = int(input('What was '  + gsteam + '\'s' + ' final score ' ))
               #find out the other team and store variable
lsteam = input ('Enter the name of the other team: ')
    #final score of ls_team
lsscore = int(input('What was ' +  lsteam  + '\'s' ' final score? ' ))
    #determine time of game
gamelength = float(input('Enter the length of the game in minutes: '))
    #calculate gs_team GPM
gsgpm = gamelength/((gsscore -150) /10)
    #calculate ls_team GPM
lsgpm = gamelength/(lsscore / 10)
    #skip line
print('\n')
    #Scoreboard
#
#
print('House\t\t\tGoals\t\tSnitch\t\tGoals Per Minute')
    #seperation line
print('=====\t\t\t=====\t\t======\t\t================')
    #print gs team with 1 under snitch and the gpm
print(gsteam ,'\t\t', (gsscore -150) / 10 , '\t\t    1','\t\t\t', format(gsgpm , '3.2f'))
    #print ls team with 0 under snitch and the gpm
print(lsteam,'\t\t', lsscore / 10,"\t\t    0",'\t\t\t', format(lsgpm,'3.2f'))
    # determine goals for the game (divide by 10 because each goal is worth 10 point in quidditch ;) )
GPG = (gsscore + lsscore - 150) / 10
    #determine average time between goals
AVG = gamelength / GPG
#
#
    #skip line
print('\n')
    #display GPG
print('Total goals for the game: ',format(GPG,'3.1f'))
    #display AVG
print('Average time between goals: ', format(AVG,'3.2f'), 'minutes')
