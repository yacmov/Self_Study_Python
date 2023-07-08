class BigNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg
    
    def __str__(self):
        return self.msg

try:
    print("Single digit division calculator")
    num1 = int(input("Type first number : "))
    num2 = int(input("Type second number : "))
    if num1 >= 10 or num2 >= 10:
        raise BigNumberError("Input : {}, {}".format(num1, num2))
    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))

except BigNumberError as err:
    print("You entered an incorrect value. Please enter only one digit number.")
    print(err)