# For loop
# For loop is used for iterating over a sequence
# Sequance : List, Tuple, Dictionary, Set, String

# Syntax
# for val in sequence
#      statments

# string
# for i in "john":
#     print(i)

# menggunakna range() function
# for i in range(5):
#     print(i)

# menambahkan starting value
# for i in range(1, 6):
#     print(i)

# menambahkan increment value
# for i in range (1, 21, 5):
#     print(i)

# decrement
# for i in range(10, 0, -2):
#     print(i)

# For loop with else
# for i in range(10):
#     print(i)
# else:
#     print("end looping")

# Break and continue
# for i in range(10):
#     if == 5:
        



# n = int(input("Masukkan jumlah angka: "))

# angka_terbesar = -float("inf")
# angka_terkecil = float("inf")
# total = 0

# for i in range(n):
#     angka = float(input("Masukkan angka ke-" + str(i + 1) + ": "))
    
#     if angka > angka_terbesar:
#         angka_terbesar = angka
#     if angka < angka_terkecil:
#         angka_terkecil = angka

#     total += angka

# rata_rata = total / n

# print("Nilai terbesar adalah: " + str(angka_terbesar))
# print("Nilai terkecil adalah: " + str(angka_terkecil))
# print("Nilai rata-rata adalah: " + str(rata_rata))
# buatlah program yang dapat menghitung total uang tabungan yang dimasukan oleh user. pertama program meminta uset memasukan jumlah hari. kemudian dengan melakukan pengulangan, minta user untuk memasukan uang tabungan harian selama jumlah hari yang sudah dimasukan sebelumnya. kemudian program akan menampilkan total uang tabungan yang dikumpulkan. (gunagakn for loop)
# contoh output: 
# masukan tabungan hari ke-1 : 5000
# masukan tabungan hari ke-2 : 10000
# masukan tabungan hari ke-3 : 20000
# masukan tabungan hari ke-4 : 50000
# masukan tabungan hari ke-5 : 10000
# total tabungan anda dalam 5 hari adalah 95000

# hari = int(input("Masukan jumlah hari: "))
# tabungan = 0
# for hari in range (1, hari + 1):
#     hari = float()

# buatlah program yang menampilkan konversi suhu celcius ke fahrenheit mulai dari 0 derajat celcius sampai 50 derajat celcius dengan penambahan 5 derajat. rumus koversi : (celcius x 9/50) = 32. (gunakan while loop)
# contoh output:
# 0 cel = 32 fah
# 5 cel = 43 fah
# 10 cel = 50 fah
# 15 cel = 59 fah
# 20 cel = 68 fah
# 25 cel = 77 fah
# 30 cel = 86 fah
# 35 cel = 95 fah
# 40 cel = 104 fah
# 45 cel = 113 fah
# 50 cel = 122 fah
# jumlah_hari = int(input("Masukkan jumlah hari: "))
# total_uang_tabungan = 0
# for hari in range(1, jumlah_hari + 1):
#     uang_harian = float(input(f"Masukkan uang tabungan hari ke-{hari}: "))
#     total_uang_tabungan += uang_harian

#     if hari == jumlah_hari:
#         print(f"Total tabungan anda dalam {jumlah_hari} hari adalah {total_uang_tabungan}")
# 2.
# celcius = 0
# penambahan = 5

# while celcius <= 50:
#     fahrenheit = (celcius * 9/5) + 32
#     print(celcius, "cel =", int(fahrenheit), "fah")
#     celcius += penambahan


jumlah_hari = int(input("Masukan jumlah hari: "))

# Inisialisasi variabel total_uang_tabungan
tabungan = 0

for hari in range(1, jumlah_hari + 1):
    uang_harian = float(input("Masukkan tabungan hari ke-" + str(hari) + " : "))
    tabungan += uang_harian

print("Total tabungan anda dalam", jumlah_hari, "hari adalah", tabungan)