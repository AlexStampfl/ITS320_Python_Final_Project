# Notes for self:
# functions are independent of classes or objects
# methods are functions tied to classes and/or objects and need an object or a 'class instance' to be invoked(such as the new_car instance at the bottom)

class Car:
    def __init__(self, make="", model="", color="", year=0, mileage=0): # constructor - for creating objects # default values so I dont' have to worry about creating arguments later on
        # private variables not to be used outside of the class
        self.__make = make
        self.__model = model
        self.__color = color
        self.__year = year
        self.__mileage = mileage


    # Getter methods - to access the private variables within the class
    def get_make(self):
        return self.__make
    def get_model(self):
        return self.__model
    def get_color(self):
        return self.__color
    def get_year(self):
        return self.__year
    def get_mileage(self):
        return self.__mileage

    
    def generate_key(self, make, model, year):
        # this is important, as there are a lot of functions that need to use the make, model, year. I believe this connects them and formats them all the same way. 
        # a little confusing but if it works it works
        return f'{make}, {model}, {year}'

    
    def removeCar(self):
        # remove car from inventory if it exists
        make = input("Enter make of car to remove: ")
        model = input("Enter model of car to remove: ")
        year = input("Enter year of car to remove: ")
        car_key = self.generate_key(make, model, year)
        
        if car_key in inventory:
            del inventory[car_key]
            print(f"Car {car_key} removed from inventory. ")
        else:
            print(f"Car {car_key} not found in inventory. ")
        self.mainMenu() # return to home page


    def updateCar(self):
        # if a car is in inventory, you can update it here
        # the update functions works almost the same as the removeCar() functions, only instead of deleting, we update the current cars
        make = input("Enter make of car to update: ")
        model = input("Enter model of car to update: ")
        year = input("Enter year of car to update: ")
        car_key = self.generate_key(make, model, year)

        if car_key in inventory:
            car = inventory[car_key]
            car.__make = input(f'Enter new make (current: {car.get_make()}) ')
            car.__model = input(f'Enter new model (current: {car.get_model()}): ')
            car.__color = input(f'Enter new color (current: {car.get_color()}): ')
            car.__year = input(f'Enter new year (current: {car.get_year()}): ')
            car.__mileage = input(f'Enter new mileage (current: {car.get_mileage()}): ')
            print(f'Car {car_key} updated.')
            self.mainMenu() # return to home page
        else:
            print(f'Car {car_key} not found in inventory. ')
            self.mainMenu() # return to home page

    
    def mainMenu(self):
        # The home page, where you can select different actions to take
        print()
        print(f'Select an action: 1) Add Car  2) Remove Car  3) Display Inventory  4) Update Car  5) Export  6) Exit')
        user_input = int(input())
        if user_input < 1 or user_input > 6:
            print(f'Please select options 1-6: {mainMenu()}')
        if user_input == 1:
            self.addCar()
        elif user_input == 2:
            self.removeCar()
        elif user_input == 3:
            self.display_details()
        elif user_input == 4:
            self.updateCar()
        elif user_input == 5:
            self.exportFile()
        else:
            print('Exiting program.')
            exit()
            # for some reason I can't use 'break' here, if says it's outside of the loop and errors out


    def display_details(self):
        if not inventory:
            print("Inventory is empty.")
            new_car.mainMenu()
        else:
            print()
            for key, car in inventory.items():
                print(f'Make: {car.get_make()}, Model: {car.get_model()}, Color: {car.get_color()}, Year: {car.get_year()}, Mileage: {car.get_mileage()}')
        print()
        # new_car.mainMenu()
        self.mainMenu() # return to home page
        # new_car.mainMenu() or self.mainMenu() will work, however self.mainMenu() is preferrable


    def addCar(self):
        # add a car to inventory
        user_make = input(f'Enter the make: ')
        user_model = input(f'Enter the model: ')
        user_color = input(f'Enter the color: ')
        user_year = input(f'Enter the year: ')
        user_mileage = input(f'Enter the mileage: ')

        # new car object with user inputs
        user_car = Car(user_make, user_model, user_color, int(user_year), int(user_mileage))
        key = self.generate_key(user_car.get_make(), user_car.get_model(), user_car.get_year())
        # add new car to inventory
        inventory[key] = user_car

        self.mainMenu() # return to home page
        return Car(user_make, user_model, user_color, user_year, user_mileage)
    
    
    def exportFile(self):
        # create a file and write the inventory to that file
        # using with, automatically closes the file after writing to it
        filename = input('Enter the filename to export the inventory: ')
        with open(filename, 'w') as file:
            for key, car in inventory.items():
                file.write(f'Make: {car.get_make()}, Model: {car.get_model()}, Color: {car.get_color()}, Year: {car.get_year()}, Mileage: {car.get_mileage()}\n')
        print(f'Inventory exported to {filename}')
        self.mainMenu() # return to home page


inventory = {}
# new instance of Car class
# no need to provide arguments as Car Class parameters have default values
new_car = Car()
# all the functions within the Car class are based off of this instance of the Car class.

new_car.mainMenu() # we call the mainMenu function, and from there, we can call all the other 

