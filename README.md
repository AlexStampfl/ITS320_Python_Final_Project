# ITS320 Python Custom Car Project
### Description
SU Global ITS320-1 Basic Programming class final project in Python. 

The Custom Car Project: Creates an automobile class that will be used by a dealership as a vehicle inventory program.
- Employs a default constructor
- a new evehicle method
- lists vehicle information
- a remove vehicle method
- a update vehicle method
- employs the use of Objects and classes
```class Car:
    def __init__(self, make="", model="", color="", year=0, mileage=0):
        # constructor - for creating objects # default values so I dont' have to worry about creating arguments later on
        # private variables not to be used outside of the class
        self.__make = make
        self.__model = model
        self.__color = color
        self.__year = year
        self.__mileage = mileage


