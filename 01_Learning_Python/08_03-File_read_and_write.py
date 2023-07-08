score_file = open("score.txt", "w", encoding="utf8")
print("Math : 0", file=score_file)
print("English : 50", file=score_file)
score_file.close()

score_file = open("score.txt", "a", encoding="utf8")
score_file.write("Sience : 80")
score_file.write("\nCoding : 100")
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
print(score_file.read()) # Output all the data
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
print(score_file.readline(), end="")
print(score_file.readline(), end="")
print(score_file.readline(), end="")
print(score_file.readline(), end="")
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
while True:
    line = score_file.readline()
    if not line:
        break
    print(line, end="")
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines()
for line in lines:
    print(line, end="")
score_file.close()