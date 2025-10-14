# create class
class Animal:
 
  # data members of class
  color = "black"     # attribute 1
  species  = "Mamalia"    # attribute 2
  name = "Anjing"
  age = "23"
  weight = "1 meter"
  location = "Manado"
  gender = "Female"
  health_status = "Sick"

  # constructor
  def __init__(self, species , color, name):
          self.species = species
          self.color = color
          self.name = name
 
  # user defined function or method
  def func(self):
          print("After calling func() method.")
          print("Species type is", self.species)
          print("Its color is", self.color)
         
  def get_name(self):
      return self.name;
     
  def get_age(self):
      return self.age;x
     
  def get_weight(self):
      return self.weight;
 
  def get_location(self):
      return self.location;
     
  def get_gender(self):
      return self.gender;
     
  def get_health(self):
      return self.health_status;
 
  def show_information(self):
      print(self.get_name());
      print(self.get_age());
      print(self.get_gender());
      print(self.get_location());
      print(self.get_health());
      print(self.get_weight());


# objects are created and the parameterized constructor is called
obj_cat = Animal('Mamalia', 'white', "cat") # object 1
obj_dog = Animal('Mamalia', 'white', 'dog') # object 2
obj_bird = Animal('Mamalia', 'white', 'bird') # object 3
obj_ular = Animal('Mamalia', 'white', 'snake') # object 3
obj_salmon = Animal('Mamalia', 'white', 'salmon') # object 3
obj_semut = Animal('Mamalia', 'white', 'ant') # object 3

# user-defined function is called from object 1
obj_cat.func()
obj_bird.show_information();
obj_ular.show_information();
obj_semut.show_information();
obj_salmon.show_information()
obj_dog.show_information()


# access the attribute
print("\nDirect access of attributes using object.")
print(obj_cat.species)
print(obj_bird)
print(obj_ular)
print(obj_semut)
print(obj_salmon)
print(obj_dog)