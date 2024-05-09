# create base class named Vehicle
class Vehicle:
    # initialization
    def __init__(self, make, miles, price, engine_on=False):
        # instance attributes/variables
        self.make = make
        self.miles = miles
        self.price = price
        self.engine_on = engine_on

    # methods
    def start_engine(self):
        self.engine_on = True
        return 'Starting engine...'

    def make_noise(self):
        return 'Beep Beep!'


# create derived class Truck
class Truck(Vehicle):
    def __init__(self, make, miles, price, cargo=False):
        # pulls from parent class Vehicle
        super().__init__(make, miles, price)
        self.cargo = cargo

    # additional load_cargo method
    def load_cargo(self):
        self.cargo = True
        return 'Loading the truck bed'


# create derived class Motorcycle
class Motorcycle(Vehicle):
    def __init__(self, make, miles, price, top_speed):
        # pulls from parent class
        super().__init__(make, miles, price)
        # set additional method of top_speed
        self.top_speed = top_speed

    # override method
    def make_noise(self):
        return 'Vroom Vroom!'


# create bike list
bikes_list = [
    Motorcycle('Harley', 0, 50000, 300),
    Motorcycle('Yamaha', 3000, 45000, 320),
    Motorcycle('Suzuki', 5000, 40000, 280)
]

# create truck list
trucks_list = [
    Truck('Ford', 200000, 5000),
    Truck('Chevy', 50000, 20000),
    Truck('Toyota', 15000, 25000)
]

# create empty list for vehicles to compare
vehicles_to_compare = []

print("Hello\nWelcome to GC Bikes and Trucks!")

# write main loop
while True:
    choice = input("Would you like to view bikes or trucks? (b or t)\n> ")
    # if choice is b for bikes
    if choice == 'b':
        print("Bikes/Motorcycles available:")
        for i in range(len(bikes_list)):
            bike = bikes_list[i]
            # display bike list
            print(f"{i + 1}. {bike.make}: with {bike.miles} miles costs ${bike.price}")
        # ask what bike they want to add to compare list
        selection = int(input("Enter the number of the bike you want to compare\n> "))
        # ensuring selection is within the range of the list
        if 1 <= selection <= len(bikes_list):
            # adds selection to vehicles to compare list
            vehicles_to_compare.append(bikes_list[selection - 1])
            print("Bike added to compare list.")
        else:
            print("Invalid Selection.")
    # if choice is t for trucks
    elif choice == 't':
        print("Trucks available:")
        for i in range(len(trucks_list)):
            truck = trucks_list[i]
            # display truck list
            print(f"{i + 1}. {truck.make}: with {truck.miles} miles costs ${truck.price}")
        selection = int(input("Enter the number of the truck you want to compare\n> "))
        if 1 <= selection <= len(trucks_list):
            vehicles_to_compare.append(trucks_list[selection - 1])
            print("Truck added to compare list.")
        else:
            print("Invalid Selection.")
    else:
        print("Invalid choice. Please enter 'b' for bikes or 't' for trucks.")

    cont = input("Do you want to continue? (y/n):\n> ")
    if cont != 'y':
        break

print('\nHere are the vehicles to compare:\n')
for vehicle in vehicles_to_compare:
    if isinstance(vehicle, Motorcycle):
        print(
            f"{vehicle.make}: with {vehicle.miles} miles costs ${vehicle.price}\n {Motorcycle.make_noise(vehicle)}")
    else:
        print(f"{vehicle.make}: with {vehicle.miles} miles costs ${vehicle.price}\n {Vehicle.make_noise(vehicle)}")

print("\nThank you for using GC Bikes and Trucks, have a nice day!")
