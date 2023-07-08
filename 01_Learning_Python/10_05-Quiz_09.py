# There is a delicious chicken restaurant in the neighborhood that always has customers waiting.
# We created an automatic ordering system to reduce the waiting time for waiting customers to cook chicken.

# Condition 1: Process as "ValueError" when an input value that is less than 1 or is not a number comes in.
#          Output message: "You entered an invalid value."

# Condition 2: The total number of chickens that waiting customers can order is limited to 10 chickens.
#          When the chicken runs out, a user-defined error (soldOutError) is generated and the program terminates.
#          Output message: "Sold out."

# [code]
# chicken = 10
# waiting = 1 # Currently full in the hall, starting from waiting number 1
# while(True):
#      print("[Remaining chicken: {0}]".format(chicken))
#      order = int(input("How many chickens would you like to order? "))
#      if order > chicken # When the order is greater than the remaining chicken
#          print("Out of stock.")
#      else:
#          print("[Waiting number {0}] {1} orders have been completed.")\
#              -format(waiting, order)
#          waiting += 1
#          chicken -= order
#
#
# 
#
class SoldOutError(Exception):
    pass

chicken = 10
waiting = 1 # Currently full in the hall, starting from waiting number 1

while (True):
    try:
        print("[Remaining chicken: {0}]".format(chicken))
        order = int(input("How many chickens would you like to order? "))
        if order > chicken: # When the order is greater than the remaining chicken
            print("Not enough chicken left order less")

        elif order <= 0:
            raise ValueError
            
        else:
            print("[Waiting number {0}] {1} orders have been completed.".format(waiting, order))
            waiting += 1
            chicken -= order
                
        if chicken == 0:
            raise SoldOutError("Sold out")

    except ValueError:
        print("You entered an invalid value.")

    except SoldOutError:
        print("Sold out")
        break


