class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        raise NotImplementedError("Subklasslar bu metodni amalga oshirish kerak")
    
    def eat(self):
        print(f"{self.name} yemoqda ")

    def sleep(self):
        print(f"{self.name} uxlamoqda")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} yurmoqda")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} hurmoqda")

class Lion(Animal):
    def speak(self):
        print(f"{self.name} sayr qilmoqda")


cat = Cat("Barsik")
dog = Dog("Pitbul")
lion = Lion("Simba")

cat.eat()    
dog.sleep()  
lion.speak() 
