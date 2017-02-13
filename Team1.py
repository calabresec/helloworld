import Fighter
import random


# here we declare your fighter
class Team1(Fighter.Fighter):

   # this is your constructor, it runs when you create your fighter
    def __init__(self, name="X"):

       # this command tells your fighter to use the constructor I made in
        # the Fighter class (which is this class's super/parent)
        super().__init__(name)

    def your_turn(self, target):

       '''
        to deal a quick attack: self.quick_attack(target)
        To deal a heavy attack: self.heavy_attack(target)
        To heal yourself:       self.heal()
        To access your name:    self.stats["name"]
        to access your health:  self.stats["health"]
        If you have more than
        50 health:              if self.stats["health"] > 50:
        If your target has less
        than 10 health:         if target.stats["health"] < 10:
        '''

       # say something cool
       print("\n{} is here to demolish you!".format(self.stats["name"]))

        if self.stats["health"] < 10:
            print("AXE IS ENRAGED")
            for x in range(3):
            self.quick_attack()
        else:
            self.heavy_attack(target)
             if target.stats["health"] <= 0:
            print("Game Over Player {} Has Won The Game!")

    def heavy_attack(self, target):
        if self.stats["charged"]:
            damage = random.randint(self.stats["strength"] / 10, self.stats["strength"] * 10)
            self.stats["charged"] = False
            print("{} hits HEAVY for ".format(self.stats["name"]) + str(damage) + " damage.")
            target.take_damage(damage)
        else:
            self.stats["charged"] = True
            print("{} prepares for a heavy attack!".format(self.stats['name']))

    def quick_attack(self, target):
        damage = random.randint(0, self.stats["strength"] * 5)
        print("{} hits for ".format(self.stats["name"]) + str(damage) + " damage.")
        target.take_damage(damage)

    def heal(self):
        '''somenumber = random.randint(0, 100)
        self.stats["health"] += somenumber
        if self.states["health"] > 100:
            self.stats["health"] = 100
        print("{} now has {} health".format(self.stats["name"], self.))'''
        poss = ["stupidity", "overkill"]
        selection = poss[random.randint(0 , len(poss))]
        if selection == "stupidity":
            print("X cannot control his ")
        self.stats["health"] += heal
        print("{} heals for {}. Total Health is {}.".format(self.stats["name"], heal, self.stats["health"]))