gun = 10

def checkpoint(solders):
    global gun
    gun = gun - solders
    print("[In function] Remaining total : {}".format(gun))

def checkpoint_ret(gun, solders):
    gun = gun - solders
    print("[In function] Remaining total : {}".format(gun))
    return gun


print("Total gun : {}".format(gun))
checkpoint(2)
print("Remaining gun : {}".format(gun))

print("Total gun : {}".format(gun))
gun = checkpoint_ret(gun, 2)
print("Remaining gun : {}".format(gun))