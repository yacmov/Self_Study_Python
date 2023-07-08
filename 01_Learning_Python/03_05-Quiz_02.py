# You recently created a new coding study group.
# I study 4 times a month, but I decided to do 3 times online and 1 time offline.

# Condition 1: Pick a date randomly
# Condition 2: Considering the difference in the number of days per month, the minimum number of days is set within 28
# Condition 3: Excluding the 1st to 3rd of every month as we need to prepare for study

# (example output statement)
# Offline study meeting date has been selected on the day X of each month.

from random import *

date = randint(4, 28)
print("Offline study meeting date has been \
selected on the day {0} of each month.".format(date))