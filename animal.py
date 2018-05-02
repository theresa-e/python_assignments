class Animal:
    def __init__(self, name, health):
        self.name = name
        self.health = health
    def walk(self):
        self.health -= 1
        return self
    def run(self):
        self.health -= 5
        return self
    def display_health(self):
        print(f"Current health: {self.health}")
        return self
class Dog(Animal):
    def __init__(self, name, health):
        super().__init__(self, name)
        self.health = 150
    def pet(self):
        self.health += 5
        return self
class Dragon(Animal):
    def __init__(self, name, health):
        super().__init__(self, name)
        self.health = 170
    def fly():
        self.health += 10
        return self
    def display_dragon(self):
        super().display_health()
        print('I am a dragon')
class Elephant(Animal):
    def __init__(self, name, health):
        super().__init__(self, name)
        self.health = 1000
    def stomp(self):
        self.health += 100
        return self


pet_cat = Animal("Theresa", 100)
cat_health = pet_cat.walk().walk().walk().run().run().display_health()

pet_dog = Dog("Puppy", 8)
pet_dog.walk().walk().walk().run().run().display_health()

pet_dragon = Dragon("Spyro", 10)
pet_dragon.display_dragon()

pet_elephant = Elephant("Andre",10)
pet_elephant.stomp().display_health