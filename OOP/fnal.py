# # # # # # # class Student:
# # # # # # #     def __init__(self, name):
# # # # # # #         self.name = name;

# # # # # # #     def info(self):
# # # # # # #         print("My name is {}.".format(self.name))

# # # # # # # if __name__ == "__main__":
# # # # # # #     Rodger = Student("Rodger Patty")
# # # # # # #     Tommy =  Student("Tommy Modoaggo")
# # # # # # #     Semmy = Student("Semmy Bambo")
# # # # # # #     Julius = Student("Julius Meisi")
# # # # # # #     Paksi = Student("Paksi Tegar")
# # # # # # #     Putri = Student("Putru Mamarimbing")

# # # # # # #     Julius.info()






# # # # # # class Person:
# # # # # #     def __init__(self, name):
# # # # # #         self.name = name 

# # # # # #     def greeting(self):
# # # # # #         print("Hello, my name is " + self.name);

# # # # # # class Student(Person):
# # # # # #     def __init__(self, name, major):
# # # # # #         super().__init__(name)
# # # # # #         self.major = major

# # # # # # s = Student("Semmy", "Computer Science")
# # # # # # s.greeting()





# # # # # class Hewan:
# # # # #     def suara(self):
# # # # #         pass

# # # # # class Kucing(Hewan):
# # # # #     def suara(self):
# # # # #         return "Meow"

# # # # # class Anjing(Hewan):
# # # # #     def suara(self):
# # # # #         return "Guk Guk"

# # # # # def panggil_suara(Hewan):
# # # # #     print(hewan.suara())

# # # # # kucing = Kucing()
# # # # # anjing = Anjing()

# # # # # panggil_suara(kucing)
# # # # # panggil_suara(anjing)






# # # # class Manusia:
# # # #     def __init__(self, nama):
# # # #         self.nama = nama
    
# # # #     def get_nama(self): 
# # # #         return self.nama

# # # #     def set_nama(self, nama):
# # # #         self.nama = nama

# # # # class Mahasiswa:
# # # #     def __init__(self, nama, jurusan):
# # # #         super().jurusan = jurusan
    
# # # #     def get_jurusan(self):
# # # #         return self.jurusan

# # # #     def set_jurusan(self, jurusan):
# # # #         self.jurusan = jurusan

# # # # mahasiswa = Mahasiswa("Semmy Taju", "Informatika", "Filkom")
# # # # print("INFORMASI AWAL YANG DINPUTKAN:")
# # # # print("Nama:", mahasiswa.get_nama())
# # # # print("Jurusan", mahasiswa.get_jurusan())

# # # # mahasiswa.set_nama("Albert Todo")
# # # # mahasiswa.set_jurusan("Sistem Informasi")
 
# # # # print("\nSETELAH PERUBAHAN INFORMASI:")
# # # # print("Nama:", mahasiswa.get_nama())
# # # # print("Jurusan", mahasiswa.get_jurusan())









# # # # import re

# # # # class GradingSystem:
# # # #     def __init__(self):
# # # #         self.grade_regex = r'[0-9]+(\.[0-9]+)?$'

# # # #     def grade(self, score):
# # # #         if re.match(self.greade_regex, score, 3):
# # # #             score = flolat(score)
# # # #             if score >= 90:
# # # #                 return 'A'
# # # #             elif score >= 80:
# # # #                 return 'B'
# # # #             elif score >= 70:
# # # #                 return 'C'
# # # #             elif score >= 60:
# # # #                 return 'D'
# # # #             else:
# # # #                 return 'E'
# # # #         else:
# # # #             return 'Invalid input'

# # # # demo = GradingSystem()

# # # # scores = ['95', '85.5', '75', '65.5', 'abc']

# # # # for score in scores:
# # # #     print(f"Score: {score}, Grade: {demo.grade(score)}")







# # # class Bentuk:
# # #     def deskripsi(self, status):
# # #         return "ini adalah bentuk geometri."

# # # class Persegi(Bentuk):
# # #     def deskripsi(self, status):
# # #         return "Ini adalah persegi."

# # # class Lingkaran(Bentuk):
# # #     def deskripsi(self, status):
# # #         return "Ini adalah lingkaran."

# # # class Segitiga(Bentuk):
# # #     def deskripsi(self, status):
# # #         return "Ini adalah segitiga."

# # # bentuk = Bentuk()
# # # persegi = Persegi()
# # # lingkaran = Lingkaran()
# # # segitiga = Segitiga()

# # # print(segitiga.deskripsi())







# # # import re as regex 
# # # input_string = "semmy@unklab.com 12/09/2024 3PM 5 orang siang"

# # # pattern = r'(\d{2})/(\d{2})(\d{4})'

# # # matches = re.search(pattern, input_string)

# # # if matches:
# # #     output = matches.group(7)
# # #     print(output)

# # # else:
# # #     print("Format tidak ditemukan")








# # class Calculator:
# #     def add(self, x, y):
# #         try:
# #             result = x + y
# #             return result
# #         except Exception as e:
# #             return f"Error: {e}"

# #     def subtract(self, x, y):
# #         try:
# #             result = x - y 
# #             return result
# #         except Exception as e:
# #             return f"error: {e}"

# #     def multiply(self, x, y):
# #         try:
# #             result = x * y
# #             return result
# #         except Exception as e:
# #             return f"Error: {e}"

# # def divide(self, x, y):
# #     try: 
# #         result = x / y
# #         return result
# #     except ZeroDivisionError:
# #         return "Error: Pembagian dengan angka not tidak diizinkan."
# #     except Exception as e:
# #         return f"Error: {e}"


# # calculator = Calculator()
# # print("Penbagian:", calculator.devide(10, 2))
    






# class Mobil:
#     def __init__(self, merk, warna):
#         self.merk = merk
#         self.warna = warna

#     def info_mobil(self):
#         return f"Mobil {self.warna} merk {self.merk}"

# class Pemilik:
#     def __init__(self, nama, mobli):
#         self.nama = nama
#         self.mobil = Mobil
    
#     def info_pemilik(self):
#         print(f"Pemilik: {self.nama}")
#         print(f"Jenis mobil: {self.mobil.info_mobil()}")


# mobil1 = Mobil("Sigra", "Hitam")
# Pemilik1 = Pemilik("Semmy Taju", mobil1)

# prmilik.info_pemilik()





class Calculator:
    def __init__(self):
        pass
    def add(self, a, b=0):
        return a + b
    def substrack(self,)