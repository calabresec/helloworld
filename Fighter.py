import random


class Fighter(object):

    # the constructor, where we set up our new fighter during instantiation
    def __init__(self, name):

        # this is called a dictionary, it's super popular in Python
        self.stats = {"name": name, "health": 100, "strength": 10, "armor": 10, "charged": False}
        print(name + " has entered the game.")
        print('Health: {} |  Strength: {}  | Armor: {} \n'
              .format(self.stats["health"], self.stats["strength"], self.stats["armor"]))

    # an attack that takes two turns, but deals guaranteed damage
    def heavy_attack(self, target):
        if self.stats["charged"]:
            damage = random.randint(self.stats["strength"] / 2, self.stats["strength"] * 2)
            self.stats["charged"] = False
            print("{} hits HEAVY for ".format(self.stats["name"]) + str(damage) + " damage.")
            target.take_damage(damage)
        else:
            self.stats["charged"] = True
            print("{} prepares for a heavy attack!".format(self.stats['name']))

    # an attack that takes only one turn, but has a chance to miss
    def quick_attack(self, target):
        damage = random.randint([0, 10] * 1.5)
        print("{} hits for ".format(self.stats["name"]) + str(damage) + " damage.")
        target.take_damage(damage)

    def heal(self):
        heal = random.randint(5, 10)
        self.stats["health"] += heal
        print("{} heals for {}. Total health: {}".format(self.stats["name"], heal, self.stats["health"]))

    def take_damage(self, dmg):
        self.stats["health"] -= dmg
        print("{} now has {} health.".format(self.stats["name"], self.stats["health"]))

    # checks if your health is above zero and returns True or False
    def is_dead(self):
        return self.stats["health"] <= 0

# end of file
