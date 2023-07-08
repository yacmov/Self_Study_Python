# print("Python", "Java", sep=" ", end="? ")
# print("What could be more fun?")

# import sys
# print("Python", "Java", file=sys.stdout) # Standard output
# print("Python", "Java", file=sys.stderr) # Standard error output

# score = {"Math":0, "English":50, "Coding":100}
# for subject, score in score.items():
#     print(subject.ljust(8), str(score).rjust(4), sep=":") 
#     #ljust(8) Get 8 spaces and align left
#     #rjust(4) Clear 4 spaces and align right

# for num in range(1, 21):
#     print("Waiting Number :" + str(num).zfill(3))

answer = input("Add anything : ")
print("The entered value is {}.".format(answer))

# When input is used, it is always stored in string form.

# If an int is needed, wrap it and store it as an int.
# answer = int(input("Add anything : "))