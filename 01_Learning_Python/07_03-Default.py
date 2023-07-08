def profile(name, age, main_lang):
    print("Name : {}\tage : {}\tMain Language: {}"\
          .format(name, age, main_lang))
    
profile("Yoo", 20, "Python")
profile("Kim", 25, "Java")

# Set up deault value 
def profile(name, age = 17, main_lang = "Python"): 
    print("Name : {}\tage : {}\tMain Language: {}"\
          .format(name, age, main_lang))
    
profile("Yoo")
profile("Kim")