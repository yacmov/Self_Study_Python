# Square brackets: []

subway1 = 10
subway2 = 20
subway3 = 30

subwayAll = [10, 20, 30]
print(subwayAll)

subwayHuman = ["Yoo", "Jo", "Pack"]
print(subwayHuman.index("Jo"))

subwayHuman.append("Haha")
print(subwayHuman)

subwayHuman.insert(1, "Jung")
print(subwayHuman)

print(subwayHuman.pop())
print(subwayHuman)

subwayHuman.append("Yoo")
print(subwayHuman)
print(subwayHuman.count("Yoo"))

num_list = [5, 2, 1, 6, 3]
num_list.sort()
print(num_list)
num_list.reverse()
print(num_list)
num_list.clear()
print(num_list)

num_list = [5, 2, 1, 6, 3]
mix_list = ["Jo", 20, True]
print(mix_list)
mix_list.extend(num_list) 
print(mix_list)