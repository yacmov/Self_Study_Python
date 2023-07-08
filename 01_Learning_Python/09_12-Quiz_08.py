# Write a real estate program using the given code.

# (Output example)
# There are a total of 3 listings.
# Gangnam apartment sales 1 billion 2010
# Mapo officetel charter 500 million 2007
# Songpa villa rent 500/50 2000

# [code]
# class House:
#     # Property initialization
#     def __init__(self, location, house_type, deal_type, price, completion_year):
#         pass

#     def show_detail(self):
#         pass


class House:
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

    def show_detail(self):
        print(self.location, self.house_type, self.deal_type,
              self.price, self.completion_year)


houses = []
house1 = House("Gangnam", "\tApartment", "\tSale",
               "\t\t$ 1,000,000", "\t\t2010")
house2 = House("Mapo\t", "\tOffice", "\t\tRent type 1",
               "\t$ 500,000", "\t\t2007")
house3 = House("Songpa\t", "\tVilla", "\t\tRent type 2",
               "\t$ 5,000 / $ 500", "\t2000")
houses.append(house1)
houses.append(house2)
houses.append(house3)

for house in houses:
    House.show_detail(house)
