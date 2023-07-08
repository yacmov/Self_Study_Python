def open_account():
    print("A new account has been created.")

def deposit(balance, money):
    print("Deposit has been completed. The balance is $ {}".format(balance + money))
    return balance + money

def withdraw(balance, money):
    if balance >= money:
        print("Withdrawal has been completed. The balance is $ {}.".format(balance - money))
        return balance - money
    else:
        print("Withdrawal has not been completed. The balance is $ {}.".format(balance))
        return balance
    
def withdraw_night(balance, money):
    commission = 100
    print("The commission is $ {}, and the balance is $ {}.".format(commission, balance - commission - money))
    return commission, balance - money - commission
    # if balance >= money:
    #     print("Withdrawal has been completed. The balance is $ {}.".format(balance - money))
    #     return balance - money
    # else:
    #     print("Withdrawal has not been completed. The balance is $ {}.".format(balance))
    #     return balance


balance = 0
balance = deposit(balance, 1000)
balance = withdraw(balance, 500)
commission, balance = withdraw_night(balance, 400)
print(balance)