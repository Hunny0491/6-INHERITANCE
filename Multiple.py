
class INDIA:
    def INDIA(self):
        print("INDIA IS VERY POWERFULL COUNTRY")

class CONTINENT:
    def CONTINENT_info(self):
        print("INDIA IS IN ASIA CONTINENT")

class WORLD(INDIA, CONTINENT):
    pass

# create an object of WORLD class
b1 = WORLD()

b1.INDIA()
b1.CONTINENT_info()

