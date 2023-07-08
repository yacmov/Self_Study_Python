from random import *            # Call the module to use       

print(random()) 		        # Generate random values ​​between 0.0 and less than 1.0
print(random() * 10) 		    # Generate random values ​​between 0.0 and less than 10.0
print(int(random()*10)) 	    # Generate random values ​​between 0 and 10
print(int(random()*10 + 1)) 	# Generates random values ​​between 1 and 10 (before 11)
print(int(random() * 45) + 1) 	# Generates random values ​​between 1 and 45 (before 46)
print(randrange(1, 46)) 	    # Outputs a random value between 1 and 45 (before 46)  
print(randint(1, 45)) 		    # Outputs the value include both ends.