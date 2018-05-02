# create a class called MathDojo
# class should have methods add and subtract (each method will take at least one parameter)
# create a new instance called md

class Math_dojo:
    def __init__(self):
        self.sum = 0
        self.sub = 0
        self.result = self.sum - self.sub
    def add(self, *nums):
        for i in nums:
            self.sum += i
        print (self.sum)
        return self
    def subtract(self, *nums):
        for i in nums:
            self.sub += i 
        print (self.sub)
        return self
        

md = Math_dojo()
md.add(2,3,2,3).subtract(2,2).result