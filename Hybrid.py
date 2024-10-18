

class vehicle:
    
    def __init__(self,model,mileage,price):
        self.price = price
        self.mileage = mileage
        self.model = model
        
    def show_details(self):
        print(f'Model : {self.model}')
        print(f'Price : {self.price}')
        print(f'Mileage : {self.mileage}')
                
class bike(vehicle):
    
    def __init__(self,model,mileage,price,tyre,cc):
        super().__init__(model,mileage,price)
        self.cc = cc
        self.tyre = tyre
    
    def show_details(self):
        super().show_details()
        print(f'CC : {self.cc}')
        print(f'Tyres : {self.tyre}')
    
   
class car(bike,vehicle):

      Royal_Enfield = bike("Continental_GT",40,345000,2,650)
      Toyota = car("Fortuner",140,500000,4,2000)

      Royal_Enfield.show_details()
      Toyota.show_details()

 