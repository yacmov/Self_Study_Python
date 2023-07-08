# customer = "Thor"
# index = 5
# while index >= 1:
#     print("[{}], Your coffee is ready. {} left".format(customer, index))
#     index -= 1
#     if index == 0:
#         print("The coffee was discarded.")

# customer = "Iron Man"
# index = 0
# while True:
#     print("[{}], Your coffee is ready. {} called  ".format(customer, index))
#     index += 1

customer = "Thor"
person = "unknown"
while person != customer:
    print("[{}], Your coffee is ready.".format(customer))
    person = input("What's your name? ")