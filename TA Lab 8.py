#Encapsulation
#The class "building" encapsulates the data "name" and "floors" and the function "building_floors".

class building:
    def __init__(self,name,floors):
        self.name = name
        self.floors = floors
    
    def building_floors(self):
        print(f"The {self.name} has {self.floors} floors.")

#Inheritance
#This class inherits the attributes "name" and "floors" from the class "building".

class apartment(building):
    def __init__(self,name,floors,units):
        super().__init__(name,floors)
        self.units = units
    
#Polymorphism
#This class overrides to modify the output string to make it fit the class apartment more as it has another attribute.

    def building_floors(self):
        print(f"The {self.name} has {self.floors} floors and {self.units} units.")

#Abstraction
#This code makes "building" into an abstract class

if __name__ == "__main__":
    apartment_building = apartment("Modern Apartment",25,100)
    apartment_building.building_floors()
    