############################################
###  DEATHMATCH - a text-based fighting game

import Fighter
import Team1

class Deathmatch(object):

    # init is used when we instantiate Deathmatch
    def __init__(self):
        print("\n ------------------------ ")
        print("---WELCOME TO DEATHMATCH---")
        print("---------------------------\n ")

        name1 = str(input("What's your first fighter's name?\n")).upper()
        # name2 = str(input("What's your second fighter's name?\n")).upper()

        fighter1 = Fighter.Fighter(name1)
        fighter2 = Team1.Team1()

        print("\n---------------------------")
        print(name1 + "  --VERSUS-- " + fighter2.stats["name"])
        print("---------------------------\n ")

        while not fighter1.is_dead():
            print("\n ~~~~~~~ IT'S YOUR TURN ~~~~~~~~")
            option = input("Heavy attack, quick attack or heal?\n").lower()
            if option == "heavy":
                fighter1.heavy_attack(fighter2)
            elif option == "quick":
                fighter1.quick_attack(fighter2)
            else:
                fighter1.heal()

            fighter2.your_turn(fighter1)

###########################
###  THE APP
###########################

game = Deathmatch()