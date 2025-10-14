# # class Employee:
# #     #constructor with parameters
# #     def __init__(self, name, age):
# #         self.name = name
# #         self.age = age
# #         self.companies = []

# #     def add_company(self, company):
# #         self.companies.append(company)

# #     def remove_company(self, company):
# #         self.companies.remove(company)

# # #class 2
# # class Company:
# #     #constructor with parameters
# #     def __init__(self, name):
# #         self.name = name
# #         self.employees = []

# #     def add_employee(self, employee):
# #         if employee not in self.employees:
# #             self.employees.append(employee)
# #             employee.add_company(self)

# #     def remove_employee(self, employee):
# #         if employee in self.employees:
# #             self.employees.remove(employee)
# #             employee.remove_company(self)

# # # membuat objek perusahaan
# # company = Company("PT Budi Mulya")

# # # membuat objek karyawan
# # employee1 = Employee("Semmy Taju", 25)
# # employee2 = Employee("Ferdy Mesakh", 30)

# # # menambahkan karyawan ke perusahaan
# # company.add_employee(employee1)
# # company.add_employee(employee2)

# # # mencetak nama karyawan dan nama perusahaan tempatnya bekerja
# # print("Karyawan 1:", employee1.name)
# # for c in employee1.companies:
# #     print("Perusahaan 1:", c.name)
# # print("Karyawan 2:", employee2.name)
# # for c in employee2.companies:
# #     print("Perusahaan 2:", c.name)

# # # mencetak nama perusahaab dan nama karyawan yang bekerja di dalamnya
# # print("Perusahaan:", company.name)
# # for e in company.employees:
# #     print("Karyawan:", e.name)

# # # menghapus karyawan dari perusahaan
# # company.remove_employee(employee1)

# # # mencetak nama karyawan dan nama perusahaan setelah di hapus
# # print("Karyawan 1:", employee1.name)
# # for c in employee1.companies:
# #     print("Perusahaan 1:", c.name)

# # print("Karyawan 2:", employee2.name)
# # for c in employee2.companies:
# #     print("Perusahaan 2:", c.name)

# # print("Perusahaan:", company.name)
# # for e in company.employees:
# #     print("Karyawan:", e.name)
# # ()


# class Animal:
#     #constructor with parametes
#     def __init__(self, name, species):
#         self.name = name
#         self.species = species
#         self.habitats = []

#     def add_habitat(self, habitat):
#         if habitat not in self.habitats:
#             self.habitats.append(habitat)
#             habitat.add_animal(self)

#     def remove_habitat(self, habitat):
#         if habitat in self.habitats:
#             self.habitats.remove(habitat)
#             habitat.remove_animal(self)

# #class 2
# class Habitat:
#     #constructor with parameters
#     def __init__(self, name):
#         self.name = name
#         self.animals = []

#     def add_animal(self, animal):
#         if animal not in self.animals:
#             self.animals.append(animal)
#             animal.add_habitat(self)

#     def remove_animal(self, animal):
#         if animal in self.animals:
#             self.animals.remove(animal)
#             animal.remove_habitat(self)


# # membuat objek zoo
# lion = Animal("Simba", "Lion")
# tiger = Animal("Rajah", "Tiger")
# monkey = Animal("Abu", "Monkey")

# # membuat objek habitat
# savanna = Habitat("Savanna")  # padang rumput
# jungle = Habitat("Jungle")  # hutan

# # Add habitats for animals
# lion.add_habitat(savanna)
# lion.add_habitat(jungle)
# tiger.add_habitat(jungle)
# monkey.add_habitat(jungle)

# # Print animals and their habitats
# print(lion.name + " lives in:")
# for habitat in lion.habitats:
#     print("- " + habitat.name)

# print(tiger.name + " lives in:")
# for habitat in tiger.habitats:
#     print("- " + habitat.name)

# print(monkey.name + " lives in:")
# for habitat in monkey.habitats:
#     print("- " + habitat.name)

# # Print habitats and their animals
# print(savanna.name + " is home to:")
# for animal in savanna.animals:
#     print("- " + animal.name + ", " + animal.species)

# print(jungle.name + " is home to:")
# for animal in jungle.animals:
#     print("- " + animal.name + ", " + animal.species)

class Book:
    # constructor with parameters
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
    
    def _str_(self):
        return f"{self.title} by {self.author}."

class Library:
    # constructor without parameter
    def __init__(self):
        self.books = []
    
    # fungsi menambah buku
    def addBook(self, book):
        print("Added this book: " + book._str_())
        self.books.append(book)
    
    # fungsi menghapus buku
    def removeBook(self, book):
        self.books.remove(book)
    
    # fungsi mencari buku berdasarkan judul
    def searchBook(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None

class Student:
    # constructor with parameter
    def __init__(self, name):
        self.name = name
        self.borrowed_book = None
        print(f"{self.name} has been registered.")
    
    # fungsi meminjam buku
    def borrowBook(self, book):
        if self.borrowed_book is None:
            self.borrowed_book = book
            print(f"{self.name} has borrowed {book.title}.")
        else:
            print(f"{self.name} has already borrowed {self.borrowed_book.title}.")
    
    # fungsi mengembalikan buku
    def returnBook(self):
        if self.borrowed_book is not None:
            print(f"{self.name} has returned {self.borrowed_book.title}.")
            self.borrowed_book = None
        else:
            print(f"{self.name} has not borrowed any book.")
    
    # fungsi menampilkan buku yang dipinjam
    def viewBorrowedBooks(self):
        if self.borrowed_book is not None:
            print(f"{self.name} has borrowed {self.borrowed_book.title}.")
        else:
            print(f"{self.name} has not borrowed any book.")

# create library object
unklab_library = Library()

print("INPUT BUKU KE PERPUSTAKAAN:")
print("===========================")

# add beberapa buku ke perpustakaan
book1 = Book("Python Programming", "Semmy Taju", "123456")
book2 = Book("Java Programming", "Green Sandag", "234567")
book3 = Book("C++ Programming", "Patricia Eugenie", "345678")

unklab_library.addBook(book1)
unklab_library.addBook(book2)
unklab_library.addBook(book3)

print("\nMAHASISWA DAFTAR DI PERPUSTAKAAN:")
print("===================================")

# create objek mahasiswa
student1 = Student("Kadek")
student2 = Student("Jeremy")
student3 = Student("Ellen")
student4 = Student("Bobby")
student5 = Student("Putra")

print("\nPROSES PINJAM BUKU DI PERPUSTAKAAN:")
print("====================================")

# meminjam buku
student1.borrowBook(book1)
student2.borrowBook(book2)
student2.borrowBook(book3)  
student3.borrowBook(book2)
student4.borrowBook(book3)
student5.borrowBook(book3)

# view buku yang dipinjam
student1.viewBorrowedBooks()
student2.viewBorrowedBooks()

# mengembalikan buku
student1.returnBook()
student2.returnBook()

# view buku yang di pinjam setelah di kembalikan
student1.viewBorrowedBooks()
student2.viewBorrowedBooks()