class bike:
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    def displayInfo(self):
        info = (f"Price: {self.price}, Max Speed: {self.max_speed}, Miles: {self.miles}")
        print (info)
    def ride(self):
        print("Riding")
        self.miles += 10
        return self
    def reverse(self):
        if self.miles >= 5:
            print("Reversing")
            self.miles -= 5
            return self
        else:
            print("Cannot reverse any further.")
            return self
 
andre = bike(100, 10)
bob = bike(400, 20)
cathy = bike(299, 15)

andre.ride().ride().ride().displayInfo()
bob.ride().reverse().reverse().displayInfo()
cathy.reverse().reverse().reverse().displayInfo()

# What would you do to prevent the instance from having negative miles?
    # If miles is equal to or greater than file, decrement the value by five. If not, print "cannot reverse any further."
# Which methods can return self in order to allow chaining methods?
    # All methods can be chained together as long as they return self. 
