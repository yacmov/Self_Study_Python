# Write a program to find the standard weight

# * Standard Weight: Appropriate weight for each individual's height

# (formula by gender)
# Male: height (m) x height (m) x 22
# Female: height (m) x height (m) x 21

# Condition 1: Standard weight is calculated within a separate function
# *Function name: std_weight
# *Transfer value: height, gender

# Condition 2: Standard weight is displayed to two decimal places

# (Output example)
# The standard weight for a man with a height of 175 cm is 67.38 kg.


def std_weight(height, gender):
    if gender == "man":
        return height * height * 22
    else:
        return height * height * 21

height = int(input("How tall you are? : "))
gender = input("Are you a man or weman? : ")
weight = round(std_weight(height / 100, gender), 2)

print("[ The standard weight for a {0} with a height of {1} cm ] : {2}kg.".format(gender, height, weight))