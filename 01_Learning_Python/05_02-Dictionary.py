# Curly braces: {}

cabinet = {3:"Yoo", 100:"Kim"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))

# print(cabinet[5]) ## Value 5 is not set, an error occurs and the program terminates
print(cabinet.get(5)) # Outputs a value of None with no 5 value set
print(cabinet.get(5, "Available")) # The value 5 is not set, so it outputs the value “Available”

print(3 in cabinet) # Check value 3 is set
print(5 in cabinet) # Check value 5 is set

cabinet = {"A-3":"Yoo", "B-100":"Kim"}
print(cabinet["A-3"])
print(cabinet["B-100"])

cabinet["A-3"] = "Kook"
cabinet["C-20"] = "Jo"
print(cabinet)

del cabinet["A-3"]
print(cabinet)

print(cabinet.keys())
print(cabinet.values())
print(cabinet.items())

cabinet.clear()
print(cabinet)