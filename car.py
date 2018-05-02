class Car:
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
    def display_all(self):
        info = f"Price: {self.price} \nSpeed: {self.speed}mph\nFuel: {self.fuel}\nMileage: {self.mileage}mpg \nTax: "
        if self.price > 10000:
            info += "0.12"
        else:
            info += "0.15"
        print (info)

car1 = Car(10000, 55, "Half full", 35)
car2 = Car(12500, 45, "Full", 28)
car3 = Car(5000, 30, "Empty", 100)
car4 = Car(10000, 105, "Full", 65)
car5 = Car(10000, 80, "Half full", 29)
car6 = Car(10000, 65, "Full", 30)
car1.display_all()
car2.display_all()
car3.display_all()
car4.display_all()
car5.display_all()
car6.display_all()