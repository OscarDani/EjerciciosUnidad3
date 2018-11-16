class Borg:
    """Borg clas making class attribute global"""
    #Attribute dictionary
    _shared_state = {}

    def __init__(self):
        #Make it an attribute dictionary
        self._dict_ = self._shared_state

class Singlenton(Borg): #Inherits from the Borg class
    """This class now share all its attributes among instances"""
    #This essenstially make singlenton objects-oriented global variable
    def __init__(self, **kwargs):
        Borg.__init__(self)
        #Update the attributes dictionary by insterting a new key-valuve pair
        self._shared_state.update(kwargs)
        
    def __str__(self):
        #Returns the attribute dictionary for printing
        return str(self._shared_state)

#Let's create a singlenton object and add our first acronym
x = Singlenton(HTTP = "Hyper Text Transform Protocol")

#print the objet
print(x)

#Let's create another singlenton object if it refers to the same attribute dictionary
#by adding another acronym
y = Singlenton(FTP = "File Transfer Protocol")
#print the object
print(y)
