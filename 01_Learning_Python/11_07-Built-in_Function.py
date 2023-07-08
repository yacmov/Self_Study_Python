# input : Functions that accept user input
language = input("what language do you like? ")
print("{} is a very nice language.".format(language))

# dir : When an object is passed, it displays which variables and functions the object has.
print(dir())
import random # exterior function
print(dir())
import pickle
print(dir())

print(dir(random))

lst = [1, 2, 3]
print(dir(lst))

name = "Jim"
print(dir(name))

# https://docs.python.org/3/library/functions.html
