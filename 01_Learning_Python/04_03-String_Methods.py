python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace("Python", "Java"))

index = python.index("n")
print(index)
index = python.index("n", index + 1)
print(index)

print(python.find("Java")) # Displays -1 even if the value is not found
print(python.index("Java")) # If the value is not found, the program terminates with an error
print(python.count("n")) # Count how many times "n" occurs in a value