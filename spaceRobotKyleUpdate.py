import random
import sys
import time


investigate = [["Trash Can 1", "Trash Blower"], ["Men's Toilet 1", "Oil Can"], ["Men's Toilet 2", "Oil Can",], ["Men's Toilet 3", "Oil Can"], ["Women's Toilet 1", "Oil Can"], ["Women's Toilet 2", "Toilet Blaster"], ["Women's Toilet 3", "Oil Can"]]
loot = ["Laboratory Key", "Corporate Bobs Office Key", "Conference Room Key", "CEO Bobs Office Key", "Spaceship Key", "Pistol", "Ray Gun", "Oil Can", "Arm Cannon",]
enemies = [["The Scientist", ["Max Health", 10], ["Health", 10], ["Base Attack", 2], ["Loot Drop", loot[0]]], ["Human", ["Max Health", 50], ["Health", 50], ["Base Attack", 10], ["Loot Drop", loot[5]]], ["Little Bob", ["Max Health", 100], ["Health", 100], ["Base Attack", 20], ["Loot Drop", loot[6]]], ["Big Bob", ["Max Health", 150], ["Health", 150], ["Base Attack", 25], ["Loot Drop", loot[1]]]]
player = ["Space Robot Kyle", ["Max Health", 100], ["Health", 100], ["Base Attack", 10], ["Attack", 10], ["Current Weapon", ""], ["Weapons", ""]]
inventory = []
miniBoss = ["Corporate Bob", ["Max Health", 200], ["Health", 200], ["Base Attack", 30], ["Loot Drop", loot[3]]]
finalBoss = ["CEO Bob", ["Max Health", 500], ["Health", 500], ["Base Attack", 40], ["Loot Drop", loot[4]]]




### START OF THE GAME ###
def start():
    print('################')
    print('Space Robot Kyle')
    print('################')
    print('A Text-Based Action/Adventure Game')
    print('By: Michael Haddad')
    print('  ')
    print('1.) New Game')
    print('2.) Exit')
    option = input('--> ')
    if option == '1':
        newGame()
    if option == '2':
        sys.exit()
    else:
        start()

def newGame():
    print('  ')
    print('''    You are Space Robot Kyle, the last robot on Earth. It's up to you to rebuild your species.
    But first you need to get a spaceship and get out of here! I hear CEO Bob has one you can 'borrow'.
    But be careful. It's dangerous out there, and the humans are out to destroy all robots. Make sure to keep
    an eye out for keys!''')
    print('  ')
    print('Your current stats are:')
    for stats in player:
        print(stats)
        time.sleep(0.5)
    print('  ')
    print('  ')
    print('Choose an option...')
    print('1.) Lobby of Starflight Enterprises')
    print('2.) Previous Menu')
    print('3.) Exit')
    print('  ')
    option = input('--> ')
    print('  ')
    if option == '1':
        lobby()
    if option == '2':
        start()
    if option == '3':
        sys.exit()
    else:
        newGame()

### ALL ROOMS ARE HERE ###

def lobby():
    print('###############################################################')
    print('You entered Starflight Enterprises. Get to the ship and escape!')
    print('###############################################################')
    print("There's an enemy! It's a scientist. Don't worry, he is a weak foe.")
    print('  ')
    print('1.) Fight')
    print('2.) Inventory')
    print("3.) Manage Weapons")
    print('4.) Main Hall')
    print('5.) Previou Menu')
    print('6.) Exit')
    option = input('-->' )
    print('  ')
    if option == '1':
        fight()
    if option == '2':
        for items in inventory:
            print(items)
            time.sleep(0.5)
    if option == '3':
        weaponsManagement()
    if option == '4':
         mainHall()
    if option == '5':
       newGame()
    if option == '6':
         sys.exit()
    else:
          lobby()       


def mainHall():
    print("You made it out of the lobby!")
    print("  ")
    print("You are now in the main hallway of Starlight Enterprises.")
    print("  ")
    print('''        You look down a long empty hallway with white walls and a white floor.
        There is a staircase at the end and doors on either side of the hallway. 
        There's is a trash can. Looks like it can be investigated... (Type 'investigate' to investigate something.)''')
    print('  ')
    print("You are free to explore!")
    print('  ')
    print("Use directional movements to move down the hallway (North/South)")
    print('  ')
    print('1.) Inventory')
    print("2.) Manage Weapons")
    print("3.) Laboratory")
    print('4.) Exit')
    option = input("--> ").lower()
    if option == "north":
        northHallway()
    if option == "south":
        lobby()
    if option == "1":
        for items in inventory:
            print(items)
            time.sleep(.5)
        mainHall()
    if option == "2":
        weaponsManagement()
    if option == "3":
        while "Laboratory Key" not in inventory:
            print("This door is locked")
            time.sleep(1)
            mainHall()
            break
        else:
            print("You unlocked the door to the laboratory!")
            time.sleep(1)
            laboratory()  
    if option == "4":
        sys.exit()
    if option == "investigate":
        print("What would you like to investigate?")
        print("  ")
        time.sleep(0.5)
        print(investigate[0][0])
        print("  ")
        option = input("--> ").lower()
        if option == "trash can 1":
            print("You found a ", investigate[0][1], "!")
            input("--> ")
            print("  ")
            print("You put the ", investigate[0][1], "in your weapons inventory.")
            player[6].append(investigate[0][1])
            input("--> ")
            mainHall()
        else:
            print("I'm sorry I didnt quite catch that...")
            time.sleep(1)
            print("  ")
            mainHall()
    else:
        print("I'm sorry I didnt quite catch that...")
        time.sleep(1)
        print("  ")
        mainHall()



def laboratory():
    print('''    You walk into a room filled with sterile countertops and beakers. 
    There are 3 enemies in front of you, and I don't think they are friendly.''')
    print('1.) Fight 1')
    print('2.) Fight 2')
    print("3.) Fight 3")
    print('4.) Inventory')
    print("5.) Manage Weapons")
    print('6.) Previous Menu')
    print('7.) Exit')
    option = input("--> ")
    if option == "1":
        fight1()
    if option == "2":
        fight2()
    if option == "3":
        fight3()
    if option == "4":
        for items in inventory:
            print(items)
            time.sleep(0.5)
        laboratory()
    if option == "5":
        weaponsManagement()
    if option == "6":
        mainHall()
    if option == "7":
        sys.exit()  
    else:
        print("I'm sorry, please choose a valid option.")
        time.sleep(1)
        laboratory()

def northHallway():
    print("There's stairs in front of you, wonder where they lead to?")            
    print("1.) Inventory")
    print("2.) Manage Weapons")
    print("3.) Men's Bathroom")
    print("4.) Women's Bathroom")
    print("5.) Exit") 
    option = input("--> ").lower()
    if option == "south":
        mainHall()
    if option == "north":
        upstairs()
    if option == "1":
        for items in inventory:
            print(items)
            time.sleep(1)
        northHallway()
    if option == "2":
        weaponsManagement()
    if option == "3":
        mensBathroom()
    if option == "4":
        womensBathroom()
    if option == "5":
        sys.exit()
    else:
        print("I'm sorry, please choose a valid option.")
        time.sleep(1)
        northHallway()    

def mensBathroom():
    print("You walk into the men's bathroom. It's empty. Maybe I can find some useful things in here if I investigate it a bit... (Type 'back' to go back)")
    option = input("--> ").lower()
    if option == "back":
        northHallway()
    if option == "investigate":
        print("What would you like to investigate?")
        print("  ")
        time.sleep(0.5)
        print(investigate[1][0])
        print(investigate[2][0])
        print(investigate[3][0])
        print("  ")
        option = input("--> ").lower()
        if option == "mens toilet 1":
            print("You found a ", investigate[1][1], "!")
            input("--> ")
            print("  ")
            print("You put the ", investigate[1][1], "in your inventory.")
            inventory.append(investigate[1][1])
            input("--> ")
            mensBathroom()
        if option == "mens toilet 2":
            print("You found a ", investigate[2][1], "!")
            input("--> ")
            print("  ")
            print("You put the ", investigate[2][1], "in your inventory.")
            inventory.append(investigate[2][1])
            input("--> ")
            mensBathroom()
        if option ==  "mens toilet 3":
            print("You found a ", investigate[3][1], "!")
            input("--> ")
            print("  ")
            print("You put the ", investigate[3][1], "in your inventory.")
            inventory.append(investigate[3][1])
            input("--> ")
            mensBathroom()
        else:
            print("I'm sorry I didnt quite catch that...")
            time.sleep(1)
            print("  ")
            mensBathroom()
    else:
        print("I'm sorry I didnt quite catch that...")
        time.sleep(1)
        print("  ")
        mensBathroom()

def womensBathroom():
    print("You walk into the women's bathroom. It's empty. Maybe I can find some useful things in here if I investigate it a bit... (Type 'back' to go back)")
    option = input("--> ").lower()
    if option == "back":
        northHallway()
    if option == "investigate":
        print("What would you like to investigate?")
        print("  ")
        time.sleep(0.5)
        print(investigate[4][0])
        print(investigate[5][0])
        print(investigate[6][0])
        print("  ")
        option = input("--> ").lower()
        if option == "womens toilet 1":
            print("You found a ", investigate[4][1], "!")
            input("--> ")
            print("  ")
            print("You put the ", investigate[4][1], "in your inventory.")
            inventory.append(investigate[4][1])
            input("--> ")
            womensBathroom()
        if option == "womens toilet 2":
            print("You found a ", investigate[5][1], "!")
            input("--> ")
            print("  ")
            print("You put the ", investigate[5][1], "in your weapons inventory.")
            player[6].append(investigate[5][1])
            input("--> ")
            womensBathroom()
        if option ==  "womens toilet 3":
            print("You found a ", investigate[6][1], "!")
            input("--> ")
            print("  ")
            print("You put the ", investigate[6][1], "in your inventory.")
            inventory.append(investigate[6][1])
            input("--> ")
            womensBathroom()
        else:
            print("I'm sorry I didnt quite catch that...")
            time.sleep(1)
            print("  ")
            womensBathroom()
    else:
        print("I'm sorry I didnt quite catch that...")
        time.sleep(1)
        print("  ")
        womensBathroom()

def upstairs():
    print("  ")
    print("You get upstairs and again, it's clear. There's a door straight ahead and two on either side of you.")
    print("1.) Inventory")
    print("2.) Manage Weapons")
    print("3.) Corporate Bob's Office")
    print("4.) CEO Bob's Office")
    print("5.) Starflight Enterprises Loading Dock")
    print("6.) Exit")
    option = input("--> ") 
    if option == "1":
        for items in inventory:
            print(items)
            time.sleep(1)
        upstairs()
    elif option == "2":
        weaponsManagement()
    elif option == "3":
        while "Corporate Bobs Office Key" not in inventory:
            print("This door is locked")
            time.sleep(1)
            upstairs()
            break
        else:
            print("You unlocked the door to Corporate Bob's Office!")
            time.sleep(1)
            corporateBobsOffice()
    elif option == "4":
        while "CEO Bobs Office Key" not in inventory:
            print("This door is locked")
            time.sleep(1)
            upstairs()
            break
        else:
            print("You unlocked the door to CEO Bob's Office!")
            time.sleep(1)
            CEOBobsOffice()
    elif option == "south":
        northHallway()
    elif option == "5":
        while "Spaceship Key" not in inventory:
            print("This door is locked")
            time.sleep(1)
            upstairs()
            break
        else:
            print("You unlocked the door to Starflight Enterprises Loading Dock!")
            time.sleep(1)
            CEOBobsOffice()
    elif option == "6":
        sys.exit()
    else:
        print("I am sorry, please type a valid response")
        upstairs()

def corporateBobsOffice():
    print("You have entered Corporate Bob's Office.")
    print('1.) Fight')
    print('2.) Inventory')
    print("3.) Manage Weapons")
    print('4.) Previous Menu')
    print('5.) Exit')
    option = input("--> ")
    if option == "1":
        fight4()
    elif option == "2":
        for items in inventory:
            print(items)
            time.sleep(1)
        corporateBobsOffice()
    elif option == "3":
        weaponsManagement()
    elif option == "4":
        upstairs()
    elif option == "5":
        sys.exit
    else:
        corporateBobsOffice()

def CEOBobsOffice():
    print("You have entered CEO Bob's Office.")
    print('1.) Fight')
    print('2.) Inventory')
    print("3.) Manage Weapons")
    print('4.) Previous Menu')
    print('5.) Exit')
    option = input("--> ")
    if option == "1":
        fight5()
    elif option == "2":
        for items in inventory:
            print(items)
            time.sleep(1)
        CEOBobsOffice()
    elif option == "3":
        weaponsManagement()
    elif option == "4":
        upstairs()
    elif option == "5":
        sys.exit

def loadingDock():
    print("You've made it to the loading dock! Hurry up! Hop in the spaceship and get out of here!")
    print("You have entered CEO Bob's Office.")
    print("1.) CEO BOB'S SPACESHIP")
    print('2.) Inventory')
    print("3.) Manage Weapons")
    print('4.) Previous Menu')
    print('5.) Exit')
    option = input("--> ")
    if option == "1":
        spaceship()
    if option == "2":
        for items in inventory:
            print(items)
            time.sleep(1)
        loadingDock()
    elif option == "3":
        weaponsManagement()
    elif option == "4":
        upstairs()
    elif option == "5":
        sys.exit

def spaceship():
    print("CONGRATS! YOU'VE WENT THROUGH THE TURMOIL AND ESCAPED SUCCESSFULLY!")
    print("YOU WIN! :) ")
    time.sleep(2)
    sys.exit()

### ALL FIGHTS ARE HERE ###
def fight():
    print(player[0], "V.S.", enemies[0][0])
    for stats in player:
        print(stats)
        time.sleep(0.05)
    print('  ')
    print("Enemy Stats: ")
    for stats in enemies[0]:
        print(stats)
        time.sleep(.05)
    print('1.) Attack')
    print('2.) Drink oil can')
    print('3.) Inventory')
    print('4.) Run')
    print("5.) Manage Inventory")
    option = input('--> ')
    print('  ')
    if option == '1':
        attack()
    if option == '2':
        drinkOil()
    if option == '3':
        print(inventory)
    if option == '4':
        run()
    if option == "5":
        weaponsManagement()
    else:
        fight()



def fight1():
    print(player[0], "V.S.", enemies[1][0])
    for stats in player:
        print(stats)
        time.sleep(0.05)
    print('  ')
    print("Enemy Stats: ")
    for stats in enemies[1]:
        print(stats)
        time.sleep(0.05)
    print('1.) Attack')
    print('2.) Drink oil can')
    print('3.) Inventory')
    print('4.) Run')
    option = input('--> ')
    print('  ')
    if option == '1':
        attack1()
    if option == '2':
        drinkOil1()
    if option == '3':
        for items in inventory:
            print(items)
    if option == '4':
        run1()
    else:
        fight1()

def fight2():
    print(player[0], "V.S.", enemies[2][0])
    for stats in player:
        print(stats)
        time.sleep(0.05)
    print('  ')
    print("Enemy Stats: ")
    for stats in enemies[2]:
        print(stats)
        time.sleep(0.05)
    print('1.) Attack')
    print('2.) Drink oil can')
    print('3.) Inventory')
    print('4.) Run')
    option = input('--> ')
    print('  ')
    if option == '1':
        attack2()
    if option == '2':
        drinkOil2()
    if option == '3':
        for items in inventory:
            print(items)
            fight2
    if option == '4':
        run2()
    else:
        fight2()

def fight3():
    print(player[0], "V.S.", enemies[3][0])
    for stats in player:
        print(stats)
        time.sleep(0.05)
    print('  ')
    print("Enemy Stats: ")
    for stats in enemies[3]:
        print(stats)
        time.sleep(0.05)
    print('1.) Attack')
    print('2.) Drink oil can')
    print('3.) Inventory')
    print('4.) Run')
    option = input('--> ')
    print('  ')
    if option == '1':
        attack3()
    if option == '2':
        drinkOil3()
    if option == '3':
        for items in inventory:
            print(items)
            fight3()
    if option == '4':
        run3()
    else:
        fight3()

def fight4():
    print(player[0], "V.S.", miniBoss[0][0])
    for stats in player:
        print(stats)
        time.sleep(0.05)
    print('  ')
    print("Enemy Stats: ")
    for stats in miniBoss:
        print(stats)
        time.sleep(0.05)
    print('1.) Attack')
    print('2.) Drink oil can')
    print('3.) Inventory')
    print('4.) Run')
    option = input('--> ')
    print('  ')
    if option == '1':
        attack4()
    if option == '2':
        drinkOil4()
    if option == '3':
        for items in inventory:
            print(items)
        fight4()
    if option == '4':
        run4()
    else:
        fight4()

def fight5():
    print(player[0], "V.S.", finalBoss[0][0])
    for stats in player:
        print(stats)
        time.sleep(0.05)
    print('  ')
    print("Enemy Stats: ")
    for stats in finalBoss:
        print(stats)
        time.sleep(0.05)
    print('1.) Attack')
    print('2.) Drink oil can')
    print('3.) Inventory')
    print('4.) Run')
    option = input('--> ')
    print('  ')
    if option == '1':
        attack5()
    if option == '2':
        drinkOil5()
    if option == '3':
        for items in inventory:
            print(items)
        fight5()
    if option == '4':
        run5()
    else:
        fight5()


### ALL ATTACK PHASES ###

def attack():
    enemyAttackChance = random.randint(0, 20)
    playerAttackChance = random.randint(0, 20)
    if playerAttackChance < 7:
        print("You missed!")
    else:
        print("A direct hit!")
        input("--> ")
        print("You deal ", player[4][1], "damage.")
        enemies[0][2][1] -= player[4][1]
    input('--> ')
    print('  ')
    if enemies[0][2][1] <= 0:
        enemies[0][2][1] = enemies[0][1][1]
        win()
    else:
        if enemyAttackChance < 7:
            print('  ')
            print('The enemy missed!')
            print('  ')
        else:
            print('Oh no! You\'ve been hit!')
            print('You take ', enemies[0][3][1], 'damage')
            print('  ')
            player[2][1] -= enemies[0][3][1]
    if player[2][1] <= 0:
        dead()
    input('--> ')


def attack1():
    enemyAttackChance = random.randint(0, 20)
    playerAttackChance = random.randint(0, 20)
    if playerAttackChance < 7:
        print("You missed!")
    else:
        print("A direct hit!")
        input("--> ")
        print("You deal ", player[4][1], "damage.")
        enemies[1][2][1] -= player[4][1]
    input('--> ')
    print('  ')
    if enemies[1][2][1] <= 0:
        enemies[1][2][1] = enemies[1][1][1]
        win1()
    else:
        if enemyAttackChance < 7:
            print('  ')
            print('The enemy missed!')
            print('  ')
        else:
            print('Oh no! You\'ve been hit!')
            print('You take ', enemies[1][3][1], 'damage')
            print('  ')
            player[2][1] -= enemies[1][3][1]
    if player[2][1] <= 0:
        dead()
    input('--> ')

def attack2():
    enemyAttackChance = random.randint(0, 20)
    playerAttackChance = random.randint(0, 20)
    if playerAttackChance < 7:
        print("You missed!")
    else:
        print("A direct hit!")
        input("--> ")
        print("You deal ", player[4][1], "damage.")
        enemies[2][2][1] -= player[4][1]
    input('--> ')
    print('  ')
    if enemies[2][2][1] <= 0:
        enemies[2][2][1] = enemies[1][1][1]
        win2()
    else:
        if enemyAttackChance < 7:
            print('  ')
            print('The enemy missed!')
            print('  ')
        else:
            print('Oh no! You\'ve been hit!')
            print('You take ', enemies[2][3][1], 'damage')
            print('  ')
            player[2][1] -= enemies[2][3][1]
    if player[2][1] <= 0:
        dead()
    input('--> ')

def attack3():
    enemyAttackChance = random.randint(0, 20)
    playerAttackChance = random.randint(0, 20)
    if playerAttackChance < 7:
        print("You missed!")
    else:
        print("A direct hit!")
        input("--> ")
        print("You deal ", player[4][1], "damage.")
        enemies[3][2][1] -= player[4][1]
    input('--> ')
    print('  ')
    if enemies[3][2][1] <= 0:
        enemies[3][2][1] = enemies[3][1][1]
        win3()
    else:
        if enemyAttackChance < 7:
            print('  ')
            print('The enemy missed!')
            print('  ')
        else:
            print('Oh no! You\'ve been hit!')
            print('You take ', enemies[2][3][1], 'damage')
            print('  ')
            player[2][1] -= enemies[2][3][1]
    if player[2][1] <= 0:
        dead()
    input('--> ')

def attack4():
    enemyAttackChance = random.randint(0, 20)
    playerAttackChance = random.randint(0, 20)
    if playerAttackChance < 7:
        print("You missed!")
    else:
        print("A direct hit!")
        input("--> ")
        print("You deal ", player[4][1], "damage.")
        miniBoss[2][1] -= player[4][1]
    input('--> ')
    print('  ')
    if miniBoss[2][1] <= 0:
        miniBoss[2][1] = miniBoss[1][1]
        win4()
    else:
        if enemyAttackChance < 7:
            print('  ')
            print('The enemy missed!')
            print('  ')
        else:
            print('Oh no! You\'ve been hit!')
            print('You take ', miniBoss[3][1], 'damage')
            print('  ')
            player[2][1] -= miniBoss[3][1]
    if player[2][1] <= 0:
        dead()
    input('--> ')

def attack5():
    enemyAttackChance = random.randint(0, 20)
    playerAttackChance = random.randint(0, 20)
    if playerAttackChance < 7:
        print("You missed!")
    else:
        print("A direct hit!")
        input("--> ")
        print("You deal ", player[4][1], "damage.")
        finalBoss[2][1] -= player[4][1]
    input('--> ')
    print('  ')
    if finalBoss[2][1] <= 0:
        finalBoss[2][1] = finalBoss[1][1]
        win5()
    else:
        if enemyAttackChance < 7:
            print('  ')
            print('The enemy missed!')
            print('  ')
        else:
            print('Oh no! You\'ve been hit!')
            print('You take ', finalBoss[3][1], 'damage')
            print('  ')
            player[2][1] -= finalBoss[3][1]
    if player[2][1] <= 0:
        dead()
    input('--> ')

### ALL WIN PHASES GO HERE ###

def win():
    print("You defeated", enemies[0][0], "!")
    print("  ")
    input("-->" )
    print("It dropped a", enemies[0][4][1])
    inventory.append(enemies[0][4][1])
    input("--> ")
    lobby()   


def win1():
    print("You defeated", enemies[1][0], "!")
    print("  ")
    input("-->" )
    print("It dropped a", enemies[1][4][1])
    player[6].append(enemies[1][4][1])
    input("--> ")
    laboratory()   

def win2():
    print("You defeated", enemies[2][0], "!")
    print("  ")
    input("-->" )
    print("It dropped a", enemies[2][4][1])
    player[6].append(enemies[2][4][1])
    input("--> ")
    laboratory()   

def win3():
    print("You defeated", enemies[3][0], "!")
    print("  ")
    input("-->" )
    print("It dropped a", enemies[3][4][1])
    inventory.append(enemies[3][4][1])
    input("--> ")
    laboratory()   

def win4():
    print("You defeated", miniBoss[0], "!")
    print("  ")
    input("-->" )
    print("It dropped a", miniBoss[4][1])
    inventory.append(miniBoss[4][1])
    input("--> ")
    corporateBobsOffice()   

def win5():
    print("You defeated", finalBoss[0], "!")
    print("  ")
    input("-->" )
    print("It dropped a", finalBoss[4][1])
    inventory.append(finalBoss[4][1])
    input("--> ")
    CEOBobsOffice()   

### ALL RUN PHASES ###
def run():
    runChance = random.randint(1, 4)
    if runChance == 1:
        print("You have successfully ran away!")
        input("--> ")
        lobby()
    else:
        print("You couldn't get away safely!")
        input("--> ")
        print('Oh no! You\'ve been hit!')
        print('You take ', enemies[0][3][1], 'damage')
        print('  ')
        player[2][1] -= enemies[0][3][1]
        if player[2][1] <= 0:
            dead()
        fight()

def run1():
    runChance = random.randint(1, 4)
    if runChance == 1:
        print("You have successfully ran away!")
        input("--> ")
        laboratory()
    else:
        print("You couldn't get away safely!")
        input("--> ")
        print('Oh no! You\'ve been hit!')
        print('You take ', enemies[1][3][1], 'damage')
        print('  ')
        player[2][1] -= enemies[1][3][1]
        if player[2][1] <= 0:
            dead()
        fight1()

def run2():
    runChance = random.randint(1, 4)
    if runChance == 1:
        print("You have successfully ran away!")
        input("--> ")
        laboratory()
    else:
        print("You couldn't get away safely!")
        input("--> ")
        print('Oh no! You\'ve been hit!')
        print('You take ', enemies[2][3][1], 'damage')
        print('  ')
        player[2][1] -= enemies[2][3][1]
        if player[2][1] <= 0:
            dead()
        fight2()

def run3():
    runChance = random.randint(1, 4)
    if runChance == 1:
        print("You have successfully ran away!")
        input("--> ")
        laboratory()
    else:
        print("You couldn't get away safely!")
        input("--> ")
        print('Oh no! You\'ve been hit!')
        print('You take ', enemies[3][3][1], 'damage')
        print('  ')
        player[2][1] -= enemies[3][3][1]
        if player[2][1] <= 0:
            dead()
        fight3()

def run4():
    runChance = random.randint(1, 4)
    if runChance == 1:
        print("You have successfully ran away!")
        input("--> ")
        corporateBobsOffice()
    else:
        print("You couldn't get away safely!")
        input("--> ")
        print('Oh no! You\'ve been hit!')
        print('You take ', miniBoss[3][1], 'damage')
        print('  ')
        player[2][1] -= miniBoss[3][1]
        if player[2][1] <= 0:
            dead()
        fight4()

def run5():
    runChance = random.randint(1, 4)
    if runChance == 1:
        print("You have successfully ran away!")
        input("--> ")
        CEOBobsOffice()
    else:
        print("You couldn't get away safely!")
        input("--> ")
        print('Oh no! You\'ve been hit!')
        print('You take ', finalBoss[3][1], 'damage')
        print('  ')
        player[2][1] -= finalBoss[3][1]
        if player[2][1] <= 0:
            dead()
        fight5()

### WHEN YOU DIE ###
def dead():
    print("YOU ARE DEAD! GAME OVER!")
    time.sleep(2)
    sys.exit()

### DRINK OIL MECHANIC ###
def drinkOil():
    if "Oil Can" not in inventory:
        print("You don't have any oil cans!")
        input("--> ")
        fight()
    else:
        print("You drank an oil can!")
        print("All lubed up!")
        if player[2][1] >= player[1][1]:
            player[2][1] = player[2][1]
        else:
            player[2][1] += 25
        
        inventory.remove("Oil Can")
        input("--> ")
        fight()          


def drinkOil1():
    if "Oil Can" not in inventory:
        print("You don't have any oil cans!")
        input("--> ")
        fight1()
    else:
        print("You drank an oil can!")
        print("All lubed up!")
        if player[2][1] >= player[1][1]:
            player[2][1] = player[2][1]
        else:
            player[2][1] += 25
        
        inventory.remove("Oil Can")
        input("--> ")
        fight1()          

def drinkOil2():
    if "Oil Can" not in inventory:
        print("You don't have any oil cans!")
        input("--> ")
        fight2()
    else:
        print("You drank an oil can!")
        print("All lubed up!")
        if player[2][1] >= player[1][1]:
            player[2][1] = player[2][1]
        else:
            player[2][1] += 25
            inventory.remove("Oil Can")
            input("--> ")
            fight2()          

def drinkOil3():
    if "Oil Can" not in inventory:
        print("You don't have any oil cans!")
        input("--> ")
        fight3()
    else:
        print("You drank an oil can!")
        print("All lubed up!")
        if player[2][1] >= player[1][1]:
            player[2][1] = player[2][1]
        else:
            player[2][1] += 25
            inventory.remove("Oil Can")
            input("--> ")
            fight3()    

def drinkOil4():
    if "Oil Can" not in inventory:
        print("You don't have any oil cans!")
        input("--> ")
        fight4()
    else:
        print("You drank an oil can!")
        print("All lubed up!")
        if player[2][1] >= player[1][1]:
            player[2][1] = player[2][1]
        else:
            player[2][1] += 25
            inventory.remove("Oil Can")
            input("--> ")
            fight4()    

def drinkOil5():
    if "Oil Can" not in inventory:
        print("You don't have any oil cans!")
        input("--> ")
        fight5()
    else:
        print("You drank an oil can!")
        print("All lubed up!")
        if player[2][1] >= player[1][1]:
            player[2][1] = player[2][1]
        else:
            player[2][1] += 25
            inventory.remove("Oil Can")
            input("--> ")
            fight5()    
### Inventory Manager ###

def weaponsManagement():
    print("In this menu, you can equip weapons.")
    print("What would you like to do?")
    print("1.) Equip Weapon")
    print("2.) Go back")
    option = input("--> ")
    if option == "1":
        equip()
    elif option == "2":
        lobby()
    else:
        weaponsManagement()


def equip():
    print("What would you like to equip? Type it in exactly the way it is shown! (Capitalization matters!)")
    for weapons in player[6]:
        print(weapons)
        time.sleep(.05)
    print("1.) Nevermind")
    option = input("--> ")
    if option == player[5][1]:
        print("You already have that weapon equipped.")
        input("--> ")
    if option == "1":
        weaponsManagement()
    if option in player[6]:
        player[5][1] = option
        print("You have equipped ", option, "!")
        print('  ')
        time.sleep(1)
        buffs()
    else:
        print("I'm sorry, that weapon does not exist.")
        weaponsManagement()


def buffs():
    if player[5][1] == "Trash Blower":
        player[4][1] = player[3][1]
        player[4][1] += 10
        weaponsManagement()
    elif player[5][1] == "Toilet Blaster":
        player[4][1] = player[3][1]
        player[4][1] += 90
        weaponsManagement()
    elif player[5][1] == "Arm Cannon":
        player[4][1] = player[3][1]
        player[4][1] += 40
        weaponsManagement()
    elif player[5][1] == "Pistol":
        player[4][1] = player[3][1]
        player[4][1] += 15
        weaponsManagement()
    elif player[5][1] == "Ray Gun":
        player[4][1] = player[3][1]
        player[4][1] += 25
        weaponsManagement()
    else:
        player[4][1] = player[3][1]
        weaponsManagement()

start()