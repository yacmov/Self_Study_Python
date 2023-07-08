absent = [2, 5]
nobook = [7]
for student in range(1, 11):
    if student in absent:
        continue
    if student in nobook:
        print("Today's class is done. {}, follow me to the office".format(student))
        break
    print("{}, read the book".format(student))