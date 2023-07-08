# A member variable is a variable defined within a class.
# You can initialize and write those variables.
class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("[Unit {}] has been created.".format(self.name))
        print("Health : {}, Attack : {}".format(self.hp, self.damage))


wraith1 = Unit("wraith", 80, 5)
print("Unit Name: {}, Damage: {}".format(wraith1.name, wraith1.damage))
# With variable name + ., you can access declared member numbers such as name and damage defined in Unit class.

wraith2 = Unit("Stolen Wraith", 80, 5)
wraith2.clocking = True

if wraith2.clocking == True:
    print("{} is the current clocking state.".format(wraith2.name))

# There is no variable called cloaking in the unit class, but it can be used by assigning a variable from the outside.