class ThailnadPackage:
    def detail(self):
        print("[Thailand Package 3 Nights 5 Days] Bangkom, Pattaya Trip (Night Market Tour) ")
        

if __name__ == "__main__":
    print("Run the Thailand module directly")
    print("This statement is only run when the module is executed directly.")
    trip_to = ThailnadPackage()
    trip_to.detail()

else:
    print("Calling all from outside Thailand")