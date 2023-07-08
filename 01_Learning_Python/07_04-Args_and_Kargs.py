# add *
def profile(name, age, *lang):
    print("이름 : {}\t나이 : {}\t".format(name, age), end=" ")
    for lang in lang:
        print(lang, end=" ")
    print()

profile("Yoo", 20, "Python", "Java", "C", "C#")
profile("Kim", 25, "Kotlin", "Swift")