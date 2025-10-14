# IF - ELSE Statment

# Pseudocode
# 1. SET temp <- 37
# 2 IF temp > 37 THEN
# 3.   DISPLAY suhu ruangan panas
# 4. ELSE
# 5.   DISPLAY

# temp = int(input("Masukan temperatur ruangan: "))
# if temp > 37: 
#     print("Suhu ruangan panas")
# else:
#     print("Suhu ruangan sejuk")

# Mini exersice
# Buat program untuk menerima input umur
# dan mengecek jika umur lebih dari atau sama dengan 17 tahun 
# Tampilakn 'anda sudah bisa buat KTP dan SIM'
# jika tidak tampilkan 'anda belum bisa buat KTP dan SIM'


# PSEUDOCODE
# 1. INPUT umur
# 2. IF umur >= 17 THEN
# 3.    DISPLAY anda sudah bisa buat KTP dan SIM
# 4. ELSE 
# 5.    DISPLAY anda belum bisa buat KTP dan SIM

age = int(input("Masukan umur anda: "))
if age >= 17:
    print("Anda sudah bisa buat KTP dan SIM")
else:
    print("Anda belum bisa buat KTP dan SIM")

# Exersice 08
# Buatlah program untuk mengecek apakah sebuah 
# bilangan yang dimasukan oleh user merupakan
# bilangan ganjil atau genap

# PSEUDOCODE 
# 1. INPUT bilangan
# 2. IF bilangan % 2 == 0
# 3.    DISPLAY bilangan genap
# 4. ELSE 
# 5.    DISPLAY bilangan ganjil
bilangan = int(input("Masukan bilangan: "))
if bilangan % 2 == 0:
    print("bilangan genap")
else:
    print("bilangan ganjil")