# using {} but no key set, just value for Set

my_set = {1,2,3,3,3}
print(my_set) # Sets ignore duplicate values.

java = {"Yoo", "Kim", "Yang"}
python = set(["Yoo", "Park"])

print(java & python) # intersection
print(java.intersection(python))

print(java | python) # union
print(java.union(python))

print(java - python) # difference
print(java.difference(python))

python.add("Kim") # add kim into python set
print(python)

java.remove("Kim") # remove kim from java set
print(java)