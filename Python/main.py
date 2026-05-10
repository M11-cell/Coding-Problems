# Basic Data Types: 

#Here we are doing type annotations btw. 
number: int = 10
decimal: float = 2.5
text: str = 'Hello world!' # Anything inside quotes. CAN BE SINGLE OR DOUBLE QUOTE. 
active: bool = False 

names: list = ['Bob', 'Aaron', 'Mike'] # Contains arbitrary amount of elements. 
coordinates: tuple = (1.5, 2.5) # Tuples are like lists, but immutable, meaning once you set the data, you CANT ADD OR REMOVE anything from it.  
unique: set = {1, 4, 9, 2} # Very similar to lists, except YOU CAN NOTTT HAVE DUPLICATES, EVERYTHING IS GUARANTEED TO BE UNIQUE
data: dict= {'name' : 'Bob', 'age': 20} # Basic wave of representing key and values. 



#Classes

# A class is just like a blueprint or a template, of how, in this example, a car should look. 
# Basically, classes can simplify the process of creating objects, or code that has to be duplicated a lot. 
class Car:

    def __init__(self, colour: str, horsepower: float) -> None: 
        # --> __init__ sets up instance of the class. aka. whem we create an object form the class we use the specific information declared in the __init__

        self.colour = colour
        self.horsepower = horsepower

    #Method are funcgions in a class ###NOTE: Self refers to the INSTANCE of the class. In this case, self referes to the volvo variable
    def drive(self) -> None: 
        print(f"Color: {self.colour}, hp = {self.horsepower}")

# This here is an instance/object of the class. 
volvo: Car = Car("green", 500.0) 

