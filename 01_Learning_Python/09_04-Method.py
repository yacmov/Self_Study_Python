class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("[Unit {}] has been created.".format(self.name))
        print("Health {}, Attack {}".format(self.hp, self.damage))

class AttackUnit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def attack(self, location):
        print("[{}] : Attacks the enemy in the direction of {}. [Attack power {}]"\
              .format(self.name, location, self.damage))
        
    def damaged(self, damage):
        print("{} : {} damaged."\
              .format(self.name, damage))
        self.hp -= damage
        print("{} : Your current health is {}".format(self.name, self.hp))
        if self.hp <= 0:
            print("{} : Destroyed".format(self.name))


firebat = AttackUnit("Firebat", 50, 16)
firebat.attack("5 o'clock")
firebat.damaged(25)
firebat.damaged(25)