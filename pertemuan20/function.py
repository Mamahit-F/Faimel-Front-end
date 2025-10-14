# Function / Fungsi

# Fungsi adalah sub-program / modul
# yang dibuat untuk menyelesaikan suatu
# tugas tertentu

# 2 jenis tugas tertentu
# 1. built-im Function -> fungsi yang sudah ada 
#                         dalan library python
#                         Contoh: print(), input()
# 2. User-defined function -> fungsi yg dibuat oleh anda sendiri


# langkah2 menggunakan fungsi:
# 1. buat / definisikan fungsi
# 2. panggil fungsi

# Definisi fungsi
# def penjumlahanDuaAngka():
#     a = 10
#     b = 20
#     hasil = a + b 
#     print("Hasil = %d" % hasil)

# # Panggil fungsi
# penjumlahanDuaAngka()

# Parameter / Argument
# def penjumlahanDuaAngka(a,b): #<- parameter
#     hasil = a + b
#     print("hasil = %d" % hasil)
# penjumlahanDuaAngka(50, 50) #<- argument
# penjumlahanDuaAngka(30, 50)

# tinggi = 1.7
# berat = 96.2
# BMI = berat/tinggi**2
# print("Tinggi: %.1f meter, Berat: %.1f Kg. BMI Anda adalah %.1f." % (tinggi, berat, BMI))

# def menghitungBMI(tinggi, berat):
#     hasil = berat/tinggi**2
#     print("Berat anda : %2f, tinggi anda adalah: %2f, BMI anda adalah %2f" % (berat, tinggi, hasil))
# menghitungBMI(1.7, 96.2)

# 4. Bentuk fungsi
# 1. Fungsi tanpa parameter dan tanpa return value

# def penjumlahanDuaAngka():
#     a = 10
#     b = 20
#     hasil = a + b
#     print("Hasil = %d " % hasil)
# penjumlahanDuaAngka()


# 2. Fungsi memilike parameter namun tanpa return value

# def penjumlahanDuaAngka(a, b):
#     hasil = a + b
#     print("Hasil = %d" % hasil)

# penjumlahanDuaAngka(10, 20)


# 3. Fungsi tanpa parameter namun memiliki return value

# def penjumlahanDuaAngka():
#     a = 10
#     b = 20
#     hasil = a + b
#     return hasil

# output = penjumlahanDuaAngka()
# print("Hasil = %d" % output)


# 4. Fungsi yang memiliki parameter dan return value

# def penjumlahanDuaAngka(a, b):
#     hasil = a + b
#     return hasil

# output = penjumlahanDuaAngka(10, 20)
# print("Hasil = %d" % output)

# Exersice 13
# 1. luas bujur sangkar (L = sisi * sisi)
# 2. luas persegi  panjang (L = panjang * lebar)
# 3. luas segitiga (L = 1/2 * alas * tinggi)
# 4. luas lingkaran (L = PHI * jari jari 8 jari jari)
