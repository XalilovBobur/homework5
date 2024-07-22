class Home:
    def __init__(self, number, price, address):
        self.number = number
        self.price = price
        self.address = address
    
    def __delattr__(self, name):
        if name == 'address':
            raise AttributeError("Bu 'address' ochirilmadi")
        super().__delattr__(name)
    
    @staticmethod
    def static_method_example():
        print("Bu static method")
       
    
    @classmethod
    def class_method_example(cls):
        print( {cls.__name__})
        

home = Home(4, 100000, "Fergana")
print(home.number)  
print(home.price)   
print(home.address) 


try:
    del home.address
except AttributeError as e:
    print(e)  


Home.static_method_example()     
Home.class_method_example()      