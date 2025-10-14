class Animal:
    def __init__(self, name):
        self.name = name
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof!"
    
class Cat(Animal):
    def make_sound(self):
        return "Meow!"
    
def test_polymorphism():
    animals = [Dog("Buddy"), Cat("Whiskers")]
    for animal in animals:
        print(animal.make_sound())
    
test_polymorphism()



# class Hewan: 
#     def suara(self):
#         pass
# class Kucing(Hewan):
#     def suara(self):
#         return "Meow"
# class Anjing(Hewan):
#     def suara(self):
#         return "Guk Guk"
# def panggil_suara(hewan):
#     print(hewan.suara())
# kucing = Kucing()
# anjing = Anjing()

# panggil_suara(kucing)
# panggil_suara(anjing)




# class Animal:
#     def __init__(self):
#         print("A")
#         self.x = 10
#     def __del__(self):
#         print("B")

# obj1 = Animal()
# obj2 = obj1
# obj3 = Animal()
# obj4 = obj3




# class Mobil:
#     def __init__(self, merk, tahun, harga):
#         self.__merk = merk
#         self.__tahun = tahun
#         self.__harga = harga

#     def get_merk(self):
#         return self.__merk
#     def get_tahun(self):
#         return self.__tahun
#     def get_harga(self):
#         return self.__harga
#     def set_harga(self, harga):
#         self.__harga = harga

# obj_mobil = Mobil("Toyota", "2022", "Rp. 5000000");



# class Human:
#     def run(self):
#         print("Method 1")

#     def see(self):
#         print("Method 2")

#     def __sleep(self):
#         print("Method 3")

#     def __funny(self):
#         print("Method 4")


# class Teacher(Human):
#     def teach(self):
#         print("I'm teaching")
#     def play(self):
#         print("I'm playing")

# obj1 = Human()
# obj2 = Teacher()