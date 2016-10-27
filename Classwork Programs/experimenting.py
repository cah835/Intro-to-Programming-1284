   #print intro
print("\t\t Welcome to CSE1284 Qudditch Calculator")
    #skip line
print('\n')
    #intro 2
print ("Enter the teams, score, and time to make it work. It's like Magic!")
    #skip line
print('\n')
    #find out winning team and store variable
gs_team = input ('Enter the name of the team that caught the golden snitch: ')
    # find out winning teams score and store as variable
gs_score =input('what was the final score of', gs_team)
    #find out the other team and store variable
ls_team = input ('Enter the name of the other team: ')
    #final score of ls_team
ls_score = float(input('what was', ls_team, 'final score? '))
    #determine time of game
game_length = float(int('Enter the length of the game: '))
    #calculate gs_team GPM
gs_gpm = ((gs_score - 150)/game_length)
    #calculate ls_team GPM
ls_gpm = (ls_score/game_length)
    #skip line
print('\n')
    #Scoreboard
print('House\t\t\t\tGoals\t\t\tSnitch\t\t\tGoals Per Minute')
    #skip line
print('\n')
