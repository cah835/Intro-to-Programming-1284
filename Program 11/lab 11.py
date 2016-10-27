import random

#class to call characters along with all atritubutes and how to level up, get potions, and use potion, def the fight function
class pyRPG_Char(object):
    def __init__(self, character_name, character_hp, character_damage):
        self.__name = character_name
        self.__hp = int(character_hp)
        self.__damage = int(character_damage)
        self.__potions = 2
        self.__nextlevel = 10
        self.__exp = 0
        self.__healingrate = 5
        self.__score = 0

    def getName(self):
        return self.__name

    def getHp(self):
        return self.__hp

    def getDamage(self):
        return self.__damage

    def getPotions(self):
        return self.__potions

    def getNextLevel(self):
        return self.__nextlevel

    def getExp(self):
        return self.__exp
    
    def getScore(self):
        return self.__score

    def lvl_up(self):
        if self.__exp >= self.__nextlevel:
            self.__exp = 0
            self.__nextlevel *= 2
            self.__hp += 1.5
            self.__damage += 1.3
            self.__healingrate += 1.3

    def usePotion(self):
        self.__hp += self.__healingrate
        self.__potions -= 1
#fight function to subtract hp, display the battle with new lines to clean up presented code
# determines winner
    def fight(self, enemy):
        while enemy.getHp() > 0 and self.__hp > 0:
            self.__hp -= enemy.getDamage()
            enemy.setHp(enemy.getHp() - self.__damage)
            print(self.__name,' lost ', enemy.getDamage(), ' hp')
            print(enemy.getName(), ' lost ', self.__damage, ' hp')
            print(self.__name, ' has ', self.__hp, ' hp')
            print(enemy.getName(), ' has ', enemy.getHp(), ' hp')
            print('\n')
        if enemy.getHp()<= 0:
            self.__exp += 2
            self.__score += enemy.getPoints()
            rdm = random.randint(1,2)
            if rdm == 1:
                self.__potions += 1
            print("You defeated him. You need ", self.__nextlevel - self.__exp, " more xp to lvl up")
            print('\n')
        

        
#creates class for enemy characters and locations to call everything needed for program
class pyRPG_enemies(object):
    def __init__(self, character):
        self.__name = character[0]
        self.__hp = int(character[1])
        self.__damage = int(character[2])
        self.__points = int(character[3])

    def getName(self):
        return self.__name

    def getHp(self):
        return self.__hp

    def getDamage(self):
        return self.__damage
    
    def getPoints(self):
        return self.__points

    def setHp(self, hp):
        self.__hp = hp

#The main function stores character into to lists and calls a the options function
def main():
    character_names = ["Tyler the Mage", "Ben the Archer", "Mrs. Henderson the Warlock", "Mr. Anderson the Warrior",
                       "Josh the Monk", "Nate the Priest"]
    character_hp = [60, 70, 80, 90, 100, 50]
    character_damage = [5, 4, 3, 2, 1, 6]
    options(character_names, character_hp, character_damage)


#This function creates a game loop that allows the user to pick two characters

def options(character_names, character_hp, character_damage):
    again = "y"
    menu = [1, 2]
    while again not in menu:
        print("1. Compare 2 characters\n2. Adventure\n3. Quit\n")
        again = input("What would you like to do: ")
        if again == "1":
            compareCharacter(character_names, character_hp, character_damage)
        elif again == "2":
            adventure(character_names, character_hp, character_damage)

#This function lets the user compare the stats for two characters
def compareCharacter(character_names, character_hp, character_damage):
    print("Pick 2 characters to compare.")
    count = 0
    for character_name in character_names:
        count += 1
        print(str(count) + ". " + character_name)
    #Let the user pick two characters and subtract 1 to get the index in the lists for those characters
    character1 = int(input("Character 1: ")) - 1
    character2 = int(input("Character 2: ")) - 1

    #Creates instances of the pyRPG class passing in (a name, a hp, a damage)
    character1 = pyRPG_Char(character_names[character1], character_hp[character1], character_damage[character1])
    character2 = pyRPG_Char(character_names[character2], character_hp[character2], character_damage[character2])
    if character1.getHp() > character2.getHp():
        print(character1.getName(), "has ", character1.getHp() - character2.getHp(), " more health than ",
              character2.getName())
    else:
        print(character2.getName(), "has ", character2.getHp() - character1.getHp(), " more health than ",
              character1.getName())
    if character1.getDamage() > character2.getDamage():
        print(character1.getName(), "has ", character1.getDamage() - character2.getDamage(), " more damage than ",
              character2.getName())
    else:
        print(character2.getName(), "has ", character2.getDamage() - character1.getDamage(), " more damage than ",
              character1.getName())


#This function allows the player to pick a character, heal, level up, and fight until the player's
#character runs out of hp
def adventure(character_names, character_hp, character_damage):
    decision_list = ["1", "2", "3"]
    count = 0
    for character_name in character_names:
        count += 1
        print(str(count) + ". " + character_name)
    player = int(input("Character: ")) - 1
    #Creates an instance of the pyRPG class passing in (a name, a hp, a damage)
    player = pyRPG_Char(character_names[player], character_hp[player], character_damage[player])
    enemy_list = [["bat", 10, 2, 5], ["rat", 15, 1, 3], ["cat", 30, 4, 10]]
    while player.getHp() > 0:
        print("1. Heal")
        print("2. Level up")
        print("3. Continue through the dungeon")
        print("You have ", player.getHp(), " hp.")
        print("You have ", player.getPotions(), " potions.")
        print("You need ", player.getNextLevel() - player.getExp(), " more xp to lvl up.")
        player_action = input("What would you like to do next? ")
        while player_action not in decision_list:
            player_action = input("What would you like to do next?")

        if player_action == "1":
            player.usePotion()
        if player_action == "2":
            player.lvl_up()
        if player_action == "3":
            enemy = pyRPG_enemies(enemy_list[random.randint(0, len(enemy_list) - 1)])
            player.fight(enemy)
    print("Game Over! You scored ", player.getScore(), " with ", player.getName())


main()

