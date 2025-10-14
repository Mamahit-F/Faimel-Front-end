    class vehicle:
        def show(self):
            print("")
            print("")
            print("Display   : Vehicle")

        def speed(self):
            print("Max speed : 150")
        
        def change_gear(self):
            print("Gear      : 5")

    class Car(vehicle):
        def show(self):
            print("Display   : Car")

        def speed(self):
            print("Max speed : 240")
        
        def change_gear(self):
            print("Gear      : 6")

    class Truck(vehicle):
        def show(self):
            print("Display   : Truck")

        def speed(self):
            print("Max speed : 200")
        
        def change_gear(self):
            print("Gear      : 8")
            print("")
            print("")

    obj_vehicle = vehicle()
    obj_mobil = Car()
    obj_truck = Truck()

    obj_vehicle.show()
    obj_vehicle.speed()
    obj_vehicle.change_gear()

    obj_mobil.show()
    obj_mobil.speed()
    obj_mobil.change_gear()

    obj_truck.show()
    obj_truck.speed()
    obj_truck.change_gear()