# Super does not support multiple inheritance.

class Unit:
     def __init__(self):
         print("Unit constructor")

class Flyable:
     def __init__(self):
         print("Flyable constructor")

class FlyableUnit(Unit, Flyable):
     def __init__(self):
         super().__init__()

dropship = FlyableUnit() # If multiple inheritance is received as Super, only the first one is received.

#alternative method
class FlyableUnit(Unit, Flyable):
     def __init__(self):
         Unit.__init__(self)
         Flyable.__init__(self)