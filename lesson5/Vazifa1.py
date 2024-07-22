class Dog:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def __setattr__(self, name, value):
        if name == 'name' and len(value) < 3:
            raise ValueError("3tadan kam bolsin")
        super().__setattr__(name, value)

try:
    dog = Dog("Bobik", 5, "qora")
except ValueError as e:
    print(f"Xato: {e}")

try:
    dog = Dog("Reks", 3, "oq")
    print("Dog:", dog.name, dog.age, dog.color)
except ValueError as e:
    print(f"Xato: {e}")
