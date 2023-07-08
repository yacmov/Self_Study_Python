from Module.travel import *
trip_to = vietnam.VietnamPackage()
trip_to.detail()
trip_to = thailand.ThailnadPackage()
trip_to.detail()

# input test module below into module file 
# if __name__ == "__main__":
#     print("Run the Thailand module directly")
#     print("This statement is only run when the module is executed directly.")
#     trip_to = ThailnadPackage()
#     trip_to.detail()

# else:
#     print("Calling all from outside Thailand")