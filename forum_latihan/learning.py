class Car:
    # variables
    def __init__(self):
            self.car_color = "Red";
            self.car_brand = "Toyota";
            self.car_year = "Tahun 2023"
    
    # methode 1 
    def carInfo(self):
        print("Car Color is {0}".format(self.car_color));
        print("Car brand is {0}".format(self.car_brand));

    # methode 2 
    def carPark(self):
        print("Parking time is over.");
        return "Return car park.!!!";

    # methode 3
    def carSpeed(self):
        print("Car speed so to fast")
        return "Return car speed.!!!";

    def carStatus(self):
       return "Ini adalah status mobil."

    # main methode
    def main(self):
        print("This is main function of class.")

        # call function
        self.carInfo();
        self.carPark();
        self.carSpeed();
        self.carStatus();

if __name__ == '__main__':
    # crate object of class
    obj_car = Car();
    obj_car.main();
    print(obj_car.car_color);
    print(obj_car.car_brand);
    print("{0}".format(obj_car.carPark()));
    print("{0}".format(obj_car.carSpeed()));


# class Car:

#     def __init__(self):
#         pass

#     car_year = "Tahun 2023"

#     def carStatus(self):
#         return "Ini adalah status mobil."

# print(Car.car_year)

# my_car = Car()
# print(my_car.carStatus())
