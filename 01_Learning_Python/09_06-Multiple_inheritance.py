# normal unit
class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
    

# attack unit
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

# Dropship: Air units, when transporting, transporting marines / firebats / tanks, etc., attack X

# Class with ability to fly
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, location):
        print("[{}] : Fly in the direction of {} . [Speed ​​{}]"\
              .format(self.name, location, self.flying_speed))
        
# Air attack unit class
class FlyableAttackUnit(AttackUnit, Flyable): #multiple inheritance
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, flying_speed)

# Valkyrie: air attack unit, 14 missiles at a time
valkyrie = FlyableAttackUnit("Valkyrie", 200, 6, 5)
valkyrie.fly("3 o'clock")