class Dog: 
    """A simple dog class"""
    def __init__(self, name):
        self._name = name
        
    def speak(self):
        return "Woof!"
    
class Cat: 
    """A simple dog class"""
    def __init__(self, name):
        self._name = name
        
    def speak(self):
        return "Meow!"

class Duck: 
    """A simple dog class"""
    def __init__(self, name):
        self._name = name
        
    def speak(self):
        return "Quack!"
    

def get_pet(pet = "dog"):
    """The factory method"""
    pets = dict(dog = Dog("Hope"), cat = Cat("King"), duck = Duck("Jane"))
    return pets[pet]

d = get_pet("dog")
print(d.speak())

c = get_pet(pet = "cat")
print(c.speak())

duck = get_pet("duck")
print(duck.speak())
    
