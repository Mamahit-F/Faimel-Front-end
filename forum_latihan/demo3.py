class Person:
    def __init__(self, name, age, address, phone_number, gender):
        self.name = name
        self.age = age
        self.address = address
        self.phone_number = phone_number
        self.gender = gender

    def view_name(self):
        return("name {}.".format(self.name))

   
    def view_age(self):
        return ("age {}.".format(self.age))

    def view_address(self):
        return  ("addrees {}.".format(self.address))

    def view_phone(self):
        return  ("phone_number {}.".format(self.phone_number))

    def view_gender(self):
        return  ("gender {}.".format(self.gender))

# Membuat objek dari class Person
person_info = Person("Faimel", "17", "Mapanget", "082177564839", "Male")

# Menggunakan method untuk menampilkan informasi
print(person_info.view_name())
print(person_info.view_age())
print(person_info.view_address())
print(person_info.view_phone())
print(person_info.view_gender())