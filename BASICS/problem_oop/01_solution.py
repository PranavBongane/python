class Car:
    totalcar = 0
    def __init__(self,brand,model):
        self.__brand = brand
        self.__model = model
        Car .totalcar+=1 

    def get_brand(self):
        return self.__brand +"!"
    
    def set_brand(self,brand):
        self.__brand = brand

    def full_name(self):
        return f"{self.__brand} {self.__model}"
    
    def fuel_type(self):
        return "petrole"
    @staticmethod
    def general_description( ):
        return"Cars are means of transport"
    @property
    def model(self):
        return self.__model

class Electric_Car(Car):
    def __init__(self,brand,model,battry_size):
        super().__init__(brand,model)
        self.battry = battry_size
    def fuel_type(self):
        return "Electric Charge"
       
my_tesla = Electric_Car("Tesla","Model s","85kwh")
my_car = Car("Toyota","Corolla")
my_tesla.set_brand("suzuki")
my_car.model = "hndjjdn"
print(my_car.model)
# print(my_tesla.general_description())
print(Car.general_description())
# print(my_tesla.get_brand())
# print(my_car.get_brand())

# print(my_tesla.fuel_type())
# print(my_car.fuel_type())
# print(Car.totalcar)

# print(my_car.brand)
# print(my_car.model)

# my_new_car = Car("Tata","Safari")
# print(my_new_car.model)
# print(my_new_car.brand)
# print(my_new_car.model)
# print(my_new_car.full_name())