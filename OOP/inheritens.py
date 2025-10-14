class Animal:
    
    __type = "Burung"
    name = "Boddy"
    age = "18"
    color = "Red"

    def __init__(self, name, age, color):

        self.name = name
        self.age = age
        self.color = color
        
    def __eat(self, type_food, time):

        self.type_food = type_food
        self.time = time
        print('Food Type:', self.type_food)
        print('Time:', self.time)

    def __run(self, duration):
        self.duration = duration
        print('Duration:', self.duration)

    def fly(self, high):

        print('High:', self.high)

    def sleep(self, time):
        print('Time:', self.time)

    def sound(self):
        print('Sound: ')

    def show(self):
        print('Name:', self.name)
        print('Color:', self.color)
    
    def data(self):
        self._Animal__eat("pelet", "pagi")
        self._Animal__run(5)

class Cat(Animal):

    __name = "Kitty"
    age = "2"

    def fly(self):
        print("Cat can't fly.")

    def sound(self):
        print("Meuw Meuw.")

    def run(self,duration):
        
        self.duration = duration
        print("Duration:", self.duration)

    def __play(self):
        print("Cat likes to run.")

    def play(self):
        self.__play()

    def data(self):
        self._Animal__eat("whiskas", "malam")
        self._Animal__run(5)

class Dog(Animal):
    
    __name = "Doggy"
    age = "3"

    def fly(self):
        print("Dog can't fly")
    
    def sound(self):
        print("Guog Guog")

    def run(self, duration):
        self.duration = duration
        print("Duration:", self.duration)

    def __play(self):
        print("Dog likes to run")

    def play(self):
        self.__play()

    def data(self):
        self._Animal__eat("daging", "siang")
        self._Animal__run(5)

class Bird(Animal):
    
    __name = "Birdy"
    age = "5"

    def fly(self):
        print("Bird can fly")
    
    def sound(self):
        print("Kiew Kiew")

    def run(self, duration):
        self.duration = duration
        print("Duration", self.duration)

    def __play(self):
        print("Bird doesn't like to run")

    def play(self):
        self.__play()

    def data(self):
        self._Animal__eat("biji-bijian", "pagi")
        self._Animal__run(5)

objek_cat = Cat("Kitty", 3, "White")
objek_dog = Dog("Doggy", 3, "Black")
objek_Bird = Bird("Birdy", 5, "Red")

print("Data Cat:")
objek_cat.show()
objek_cat.fly()
objek_cat.sound()
objek_cat.run(5)
objek_cat.play()
objek_cat.data()
print()

print("Data Dog:")
objek_dog.show()
objek_dog.fly()
objek_dog.sound()
objek_dog.run(8)
objek_dog.play()
objek_dog.data()
print()

print("Data Bird:")
objek_Bird.show()
objek_Bird.fly()
objek_Bird.sound()
objek_Bird.run(10)
objek_Bird.play()
objek_Bird.data()
print()