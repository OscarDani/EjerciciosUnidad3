# AbstractFactory.py

class Dog: 
    """A simple dog class"""
  
        
    def speak(self):
        return "Woof!"

    def __str__(self):
        return "Dog"

class Cat: 
    """A simple cat class"""
        
    def speak(self):
        return "Maow!"

    def __str__(self):
        return "Cat"

class CatFactory:
    """Concrete Factory"""
    def get_pet(self):
        """Return a Cat object"""
        return Cat()

    def get_food(self):
        """Return a Cat food objetc"""
        return "Fishes"

class DogFactory:
    """Concrete Factory"""
    def get_pet(self):
        """Return a Dog object"""
        return Dog()


    def get_food(self):
        """Return a Dog food objetc"""
        return "Chiken"

class PetStore:
    """PetStore houses our Abstract Factory"""
    def __init__(self, pet_factory = None):
        """pet_factoy ia our Abstract Factory"""
        self._pet_factory = pet_factory

    def show_pet(self):
        """Utility method to display the details of the objects by the factory"""
        pet = self._pet_factory.get_pet()
        pet_food = self._pet_factory.get_food()
        
        print("Our pet is '{}'".format(pet))
        print("Our pet say hello by '{}'".format(pet.speak()))
        print("Its food is'{}'".format(pet_food))
    def set_factory(self, pet_factory):
        self._pet_factory = pet_factory
        

#Create a concrete factory
factory = DogFactory()
#Create a pet store housing our abstract factory
shop = PetStore(factory)
shop.show_pet()
#Create a Cat factory
cat_factory = CatFactory()
shop.set_factory(cat_factory)
shop.show_pet()
