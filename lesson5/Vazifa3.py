class Cat:
    def __init__(self, name, age, color):
        self.__dict__['name'] = name  
        self.__dict__['age'] = age
        self.__dict__['color'] = color

    def __setattr__(self, name, value):
        if name not in ['name', 'age', 'color']:
            raise AttributeError(f"'Cat' object has no attribute '{name}'")
        else:
            self.__dict__[name] = value

    def __delattr__(self, name):
        if name in ['name', 'age', 'color']:
            raise AttributeError(f"'Cat' attribute '{name}' cannot be deleted")
        else:
            super().__delattr__(name)

    def __getattr__(self, name):
        if name in ['name', 'age', 'color']:
            return self.__dict__[name]
        else:
            raise AttributeError(f"'Cat' object has no attribute '{name}'")

    def __getattribute__(self, name):
        if name in ['name', 'age', 'color']:
            return object.__getattribute__(self, name)
        else:
            raise AttributeError(f"'Cat' object has no attribute '{name}'")



cat = Cat('Momiq', 2, 'kulrang')


print(cat.name)   
print(cat.age)    
print(cat.color)  


try:
    cat.size = 'small'
except AttributeError as e:
    print(f"Xato: {e}")   #qoshish bloklandi


try:
    del cat.age
except AttributeError as e:
    print(f"Xato: {e}") #ochirish bloklandi

try:
    print(cat.weight)
except AttributeError as e:
    print(f"Xato: {e}") 