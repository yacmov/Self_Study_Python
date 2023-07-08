#building
class BuildingUnit(Unit):
     def __init__(self, name, hp, location):
         pass

#Supply Depot: Building, 1 construction = 8 units.
supply_depot = BuilingUnit("Supply Depot", 500, "7 o'clock")

def game_start():
     print("[NOTICE] Starting a new game.")

def game_over():
     pass

game_start()
game_over()