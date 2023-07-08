# normal unit
class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
    

# Attack unit
class AttackUnit(Unit):
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp)
        self.damage = damage

    def attack(self, location):
        print("[{}] : Attacks the enemy in the direction of {}. [Attack power {}]"\
              .format(self.name, location, self.damage))
        
    def damaged(self, damage):
        print("[{}] : {} damaged."\
              .format(self.name, damage))
        self.hp -= damage
        print("[{}] : Your current health is {}".format(self.name, self.hp))
        if self.hp <= 0:
            print("[{}] : Destroyed".format(self.name))