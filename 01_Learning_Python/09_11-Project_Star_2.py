from random import *

# normal unit
class Unit:
     def __init__(self, name, hp, speed):
         self.name = name
         self.hp = hp
         self. speed = speed
         print("[Unit {}] has been created.".format(name))

     def move(self, location):
         print("Move nomal units")
         print("[{}] : Move in the direction of {} direction. [Speed {}]"\
               .format(self.name, location, self.speed))
        
     def damaged(self, damage):
         print("[{}] : {} damaged."\
               .format(self.name, damage))
         self.hp -= damage
         print("[{}] : Your current health is {}".format(self.name, self.hp))
         if self.hp <= 0:
             print("[{}] : Destroyed".format(self.name))

# attack unit
class AttackUnit(Unit):
     def __init__(self, name, hp, speed, damage):
         Unit.__init__(self, name, hp, speed)
         self.damage = damage

     def attack(self, location):
         print("[{}] : Attacks the enemy in the direction of {}. [Attack power {}]"\
               .format(self.name, location, self.damage))

# Dropship: Air units, when transporting, transporting marines / firebats / tanks, etc., attack X

# Class with ability to fly
class Flyable:
     def __init__(self, flying_speed):
         self.flying_speed = flying_speed

     def fly(self, location, flying_speed):
         print("[{}] : Fly in the direction of {} direction. [Speed {}]"\
               .format(self.name, location, self.flying_speed))
        
# Air attack unit class
class FlyableAttackUnit(AttackUnit, Flyable): #multiple inheritance
     def __init__(self, name, hp, damage, flying_speed):
         AttackUnit.__init__(self, name, hp, 0, damage) # Treat ground speed as 0
         Flyable.__init__(self, flying_speed)

     def move(self, location):
         print("Move air units")
         self.fly(self.name, location)

# Marine
class Marine (AttackUnit):
     def __init__(self):
         AttackUnit.__init__(self, "Marine", 40, 1, 5)
    
     # Steam Pack
     def stimpack(self):
         if self.hp > 10:
             self.hp -= 10
             print("[{}] : Use stimpak. (HP reduced by 10)".format(self.name))
         else:
             print("[{}] : Stimpack is not used due to insufficient stamina.".format(self.name))

# Tank
class Tank(AttackUnit):
     seize_developed=False

     def __init__(self):
         AttackUnit.__init__(self, "Tank", 150, 1, 35)
         self.seize_mode = False

     def set_seize_mode(self):
         if Tank.seize_developed == False:
             return
        
         if self.set_seize_mode == False:
             print("[{}] : Release to Siege Mode.".format(self.name))
             self.damage /= 2
             self.set_seize_mode = True
         else:
             print("[{}] : Switch to Siege Mode.".format(self.name))
             self. damage *= 2
             self.set_seize_mode = False

# wraith
class wraith(FlyableAttackUnit):
     def __init__(self):
         FlyableAttackUnit.__init__(self, "Wraith", 80, 20, 5)
         self.clocked = False

     def clocking(self):
         if self. clocked == True:
             print("[{}] : Disable clocking mode.".format(self.name))
             self.clocked = False
         else:
             print("[{}] : Set clocking mode.".format(self.name))
             self. clocked = True

def game_start():
     print("[NOTICE] Starting a new game.")

def game_over():
     print("Player: gg")
     print("[Player] has left the game.")


game_start()
m1 = Marine()
m2 = Marine()
m3 = Marine()
t1 = Tank()
t2 = Tank()
w1 = wraith()

attack_units = []
attack_units. append(m1)
attack_units. append(m2)
attack_units. append(m3)
attack_units. append(t1)
attack_units. append(t2)
attack_units. append(w1)

for unit in attack_units:
     unit.move("1 o'clock")

Tank.seize_developed = True
print("[Notice] Tank Siege mode development has been completed.")

for unit in attack_units:
     if isinstance(unit, Marine):
         unit. stimpack()
     elif isinstance(unit, Tank):
         unit.set_seize_mode()
     elif isinstance(unit, wraith):
         unit. clocking()

for unit in attack_units:
     unit.attack("1 o'clock")

for unit in attack_units:
     unit.damaged(randint(5, 21))

game_over()