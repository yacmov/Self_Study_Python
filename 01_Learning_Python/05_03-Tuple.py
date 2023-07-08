# Parentheses: () (AKA "round brackets")

menu = ("Katsu Don", "Katsu Cheese")
print(menu[0])
print(menu[1])

#menu.add("Katsu Fish") ## If defined as a tuple, no addition

name = "Kim"
age = 20
hobby = "coding"
print(name, age, hobby)
values = (name, age, hobby)
print(type(values))

(name, age, hobby) = ("Kim2", 202, "coding2")
values = (name, age, hobby)
print(type(values))
