# try:
#     print("Division calculator")
#     num1 = int(input("Type first number : "))
#     num2 = int(input("Type second number : "))
#     print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))

# except ValueError:
#     print("An error occurred \"Wrong Value\"")
# except ZeroDivisionError as err:
#     print(err)

# try:
#     print("Division calculator")
#     nums = []
#     nums.append(int(input("Type first number : ")))
#     nums.append(int(input("Type first number : ")))
#     nums.append(int(nums[0] / nums[1]))

#     print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))

# except ValueError:
#     print("An error occurred \"Wrong Value\"")
# except ZeroDivisionError as err:
#     print(err)

try:
    print("Division calculator")
    nums = []
    nums.append(int(input("Type first number : ")))
    nums.append(int(input("Type first number : ")))
    # nums.append(int(nums[0] / nums[1]))

    print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))

except ValueError:
    print("An error occurred \"Wrong Value\"")
except ZeroDivisionError as err:
    print(err)
# except: # Output when all other errors occur
#     print("An unknown error occurred")

except Exception as err: # Output when all other errors occur
    print("An unknown error occurred")
    print(err)