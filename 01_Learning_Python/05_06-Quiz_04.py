# Your school hosts a Python coding competition.
# We decided to hold a comment event to increase the attendance rate.
# Among the commenters, 1 person will receive a chicken and 3 coffee coupons through a lottery.

# Condition 1: For convenience, it is assumed that 20 comments have been written and IDs are 1-20.
# Condition 2: Random draw regardless of comment content, but no duplicates
# Condition 3: Utilize random module's shuffle and sample

# (Output example)
# -- Announcement of winners --
# Chicken Winner: 1
# Coffee Winners: 2, 3, 4
# -- congratulations --

from random import *
id = list(range(1,21))
shuffle(id)
winners = sample(id, 4)
print("-- Announcement of winners --")
print("Chicken Winner: {0}".format(winners[0]))
print("Coffee Winners: {0}, {1}, {2}".format(winners[1], winners[2], winners[3]))
print("-- congratulations --")