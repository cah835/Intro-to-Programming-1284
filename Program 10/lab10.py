# Corey Henry & Geoffrey Sanchez              # Date Assigned: 12Nov14
#                                             #
# Course CSE 1284 Sec 02                      # Date Due: 19Nov2014
# File name: lab10.py
#
# Program description - open a list to run to iso file and create and add more characters 

#create class
class Characters:
#intialize the object
    def __init__(self, name, hp, damage):
        self.__name = name
        self.__hp = hp
        self.__damage = damage
 #function to get the name from the list        
    def get_name(self):
        return self.__name
#function to get the hp for list
    def get_hp(self):
        return self.__hp
#function to get the damage from the list
    def get_damage(self):
        return self.__damage
#function to add a name in the list
    def set_name(self, name):
        self.__name = name
#function to add hp in the list
    def set_hp(self, hp):
        self.__hp = hp
#function to add damage into the list
    def set_damage(self, damage):
        self.__damage = damage

#create main function and call functions to run
def main():
    characters_list = []
    read_file(characters_list)
    menu(characters_list)
# open the file and strip the lines and split it up into name, hp, and damage
def read_file(characters_list):
    inFile = open("fileio.txt")
    for each_line in inFile:
        each_line = each_line.strip()
        if each_line == "character_info setup: name, hp, damage":
            continue
        name, hp, damage = each_line.split(', ')
        character = Characters(name, hp, damage)
        characters_list.append(character)
#close the file
    inFile.close()
#create the menu
def menu(characters_list):
    print("1. Compare 2 characters")
    print("2. Create a new character")
    print("3. Quit")

    
#validation loop
    flag = False
    while flag == False:
        choice = int(input("What would you like to do: "))
        if choice == 1 or choice == 2 or choice == 3:
            flag = True
        else:
            print("ERROR: enter a valid choice")
#if statements that lead to the different functions
    if choice == 1:
        print("")
        compare_characters(characters_list)
    elif choice == 2:
        print("")
        create_characters(characters_list)
    elif choice == 3:
        quit

        
#function to compare the characters
def compare_characters(characters_list):
    print("Pick 2 characters to compare.")
    for each in range(len(characters_list)):
        print(str(each + 1) + ". " + characters_list[each].get_name())

#validation loop
    flag = False
    while flag == False:
        character_1 = int(input("Character 1: "))
        if character_1 > 0 and character_1 < len(characters_list) + 1:
            flag = True
        else:
            print("ERROR: enter a valid choice")
#validation loop
    flag = False
    while flag == False:
        character_2 = int(input("Character 2: "))
        if character_2 > 0 and character_2 < len(characters_list) + 1:
            flag = True
        else:
            print("ERROR: enter a valid choice")
#if and else statments to determine which character goes first and do the math involved and print answer
    if int(characters_list[character_1 - 1].get_hp()) < int(characters_list[character_2 - 1].get_hp()):
        diff = int(characters_list[character_2 - 1].get_hp()) - int(characters_list[character_1 - 1].get_hp())
        print(characters_list[character_2 - 1].get_name() + " has " + str(diff) + " more health than " + characters_list[character_1 - 1].get_name())
    else:
        diff = int(characters_list[character_1 - 1].get_hp()) - int(characters_list[character_2 - 1].get_hp())
        print(characters_list[character_1 - 1].get_name() + " has " + str(diff) + " more health than " + characters_list[character_2 - 1].get_name())

    if int(characters_list[character_1 - 1].get_damage()) < int(characters_list[character_2 - 1].get_damage()):
        diff = int(characters_list[character_2 - 1].get_damage()) - int(characters_list[character_1 - 1].get_damage())
        print(characters_list[character_2 - 1].get_name() + " has " + str(diff) + " more damage than " + characters_list[character_1 - 1].get_name())
    else:
        diff = int(characters_list[character_1 - 1].get_damage()) - int(characters_list[character_2 - 1].get_damage())
        print(characters_list[character_1 - 1].get_name() + " has " + str(diff) + " more damage than " + characters_list[character_2 - 1].get_name())
#call menu to create a continuous loop
    print("")
    menu(characters_list)
# function to create a new character and add him to the file
def create_characters(characters_list):      
    name = input("Name: ")
    hp = input("HP: ")
    damage = input("Damage: ")

    character = Characters(name, hp, damage)
    characters_list.append(character)
#open file to add new inofrmation
    inFile = open("fileio.txt", 'a+')
#write information in to the file and close it
    inFile.write("\n" + name + ", " + hp + ", " + damage)
    inFile.close()
#call menu to continue contious loop
    print("")
    menu(characters_list)
    
main()
