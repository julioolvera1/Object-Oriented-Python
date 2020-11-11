## Objects within objetcs
## Pets and owners

class Pet():

    def __init__(self,species,name):

        self.species=species
        self.name=name

        ## Initially pet has no owner
        self.owner=None

class Person():

    def __init__(self,name):
        self.name=name
        self.pets=[]

    def add_pet(self,pet):
        self.pets.append(pet)

        ## This line causes pet.owner to be a reference to the Person object
        pet.owner=self

    
person_1=Person('Julio')

tony=Pet('Dog','Aki')

person_1.add_pet(tony)

print(person_1.pets[0].name)

print(tony.owner.name)
