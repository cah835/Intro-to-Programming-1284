## do not change anything in here!!!!
## go to run program, you should not have to save it to run it!
## put the grades you have recieved already and the grades you hope to get.
# it will print out your grade number and letter grade for the class




print("Welcome to Dr.Dornshuld's Chemistry Calculator")
again = 'y'
while again == 'y':
    print('\n')
    homework = int(input('What is your averaged homework grade? '))
    test1 = int(input('What is your first test grade? '))
    test2 = int(input('What is your 2nd test grade? '))
    test3 = int(input('What is your 3rd test grade? '))
    final = int(input('What is your final exam grade? '))
    tests = test1+test2+test3+final
    test = tests/4
    final_grade = homework *.10 + 100*.05 + test * .8501
    final_grade = round(final_grade,0)
    print('This grade is based off of PERFECT Attendance')
    if final_grade <= 54.0:
        letter_grade = 'F'
    elif final_grade >= 55.0 and final_grade <= 64.0:
        letter_grade = 'D'
    elif final_grade >= 65 and final_grade <= 74.0:
        letter_grade = 'C'
    elif final_grade >= 75.0 and final_grade <= 84.0:
        letter_grade = 'B'
    elif final_grade >= 85.0:
        letter_grade = 'A'
    print('Final Grade: ', final_grade,'Letter Grade: ', letter_grade)
    again = input('Would you like try again?(y/n): ')
    if again != 'y':
        quit
