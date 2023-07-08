# name = "Marine" # the name of the unit
# hp = 40 # Health Point
# damage = 5 # Unit's damage

# print("[Unit {0}] has been created.".format(name))
# print("HP {0}, ATK {1}".format(hp, damage))

# tank_name = "Tank"
# tank_hp = 150
# tank_damage = 35

# print("[Unit {0}] has been created.".format(tank_name))
# print("HP {0}, ATK {1}".format(tank_hp, tank_damage))


# tank2_name = "Tank"
# tank2_hp = 150
# tank2_damage = 35

# print("[Unit {0}] has been created.".format(tank2_name))
# print("HP {0}, ATK {1}".format(tank2_hp, tank2_damage))


# def attack(name, location, damage):
# print("[{}] : Attacks the enemy in the direction of {}. [Attack power {}]"\
# .format(name, location, damage))
    
# attack(name, "1 o'clock attack", damage)
# attack(tank_name, "1 o'clock attack", tank_damage)
# attack(tank2_name, "1 o'clock attack", tank2_damage)

class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("[Unit {}] has been created.".format(self.name))
        print("Health : {}, Attack : {}".format(self.hp, self.damage))

marine1 = Unit("Marine", 40, 5)
marine2 = Unit("Marine", 40, 5)
tank1 = Unit("Tank", 150, 35)