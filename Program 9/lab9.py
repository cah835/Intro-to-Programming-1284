#Corey Henry & Geoffrey Sanchez              #Date Assigned: 05Nov14
#                                            #
#Course CSE 1284 Sec 02                      #Date Due: 12Nov2014
#File name: lab9.py
#
#Program description -  develop a calculator to determine the average test
#and quiz grades.

#define the main function
def main():
    print('Grade Calculator')
    print('----------------')
    again = 'y'
    while again != 'n':
        #get the name from the user and open the file
        file_name = input("Please enter the grade file you wish to calculate: ")
#add .txt to end of the file if the user forgets
        if not file_name.endswith(' .txt'):
            file_name += '.txt'

        flag = True

        while flag:
            try:
                original = open(file_name)
            except FileNotFoundError as error:
                print('Invalid file name. ')
                file_name = input('please re-enter ')
                if not file_name.endswith(' .txt'):
                    file_name += '.txt'
            else:
                flag = False
#set up the lists with no values for each of the types of grades.
        quiz_list = []

        lab_list = []

        test_list = []

        final_list = []

        current = 0
#use a loop to determine which grades go into each list by using the name to seperate each list
        for each_line in original:
            if each_line.endswith("Quizzes and Assignments\n"):
                current = 1
            elif each_line.endswith('Lab Assignments\n'):
                current = 2
            elif each_line.endswith('Tests\n'):
                current = 3
            elif each_line.endswith('Final Exam\n'):
                current = 4
            try:
                number = int(each_line.strip())
            except ValueError as error:
                continue
            else:
                if current == 1:
                    quiz_list.append(number)
                elif current == 2:
                    lab_list.append(number)
                elif current == 3:
                    test_list.append(number)
                elif current == 4:
                    final_list.append(number)

    
    #Computation to find out the average of each list and them up according to percents to get a final grade
        average_quizz_list = sum(quiz_list)/len(quiz_list)
        average_lab_list = sum(lab_list)/len(lab_list)
        average_test_list = sum(test_list)/len(test_list)
        final_grade = 0.2 * average_quizz_list + 0.15 * average_lab_list + 0.45 * average_test_list + 0.20 * final_list[0]
# print final grade with format to round up
        print('Final Grade: %.0f' % final_grade)
#prompt user if he would like to add another file
        again = input('Would you like to enter another file name? (y/n) ')
        print('-----------------------------------------------------')
        
main()
