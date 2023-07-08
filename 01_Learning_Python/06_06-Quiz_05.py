# You are a taxi driver using the Uber service.
# Write a program to find the total number of passengers on board when there are 50 passengers and matching opportunities.

# Condition 1: Travel time per passenger is determined by a random number between 5 and 50 minutes.
# Condition 2: You must only match passengers between 5 and 15 minutes in travel time.

# (Output statement example)
# [O] Customer 1 (Time required: 15 minutes)
# [ ] Customer 2 (Time required: 50 minutes)
# [O] Customer 3 (Time required: 5 minutes)
# ...
# [ ] Customer 50 (Time required: 16 minutes)

# Total boarding passengers: 2 minutes

from random import *

boardingcustomers = 0

for i in range(1,51):
    time = randint(5, 50)
    # print(travel_time)
    if 5 <= time <= 15:
        print("[O] Customer {0} (Time required: {1} minutes)".format(str(i).zfill(2), str(time).zfill(2)))
        boardingcustomers += 1
    else:
        print("[ ] Customer {0} (Time required: {1} minutes)".format(str(i).zfill(2), str(time).zfill(2)))


print("Total boarding passengers: {0} ".format(boardingcustomers))