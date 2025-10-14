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

# Exercise #13
# Buatlah program yang dapat menghitung:
# 1. Luas bujur sangkar (L = sisi * sisi) -> Bentuk 1
# 2. Luas persegi panjang (L = panjang * lebar) -> Bentuk 2
# 3. Luas segitiga (L = 1/2 * alas * tinggi) -> Bentuk 3
# 4. Luas Lingkaran (L = PHI * jari2 * jari2) -> Bentuk 4import math

def hitung_luas_bujur_sangkar():
    sisi = float(input("Masukkan panjang sisi bujur sangkar: "))
    luas = sisi * sisi
    print("Luas bujur sangkar adalah:", luas)

def hitung_luas_persegi_panjang():
    panjang = float(input("Masukkan panjang persegi panjang: "))
    lebar = float(input("Masukkan lebar persegi panjang: "))
    luas = panjang * lebar
    print("Luas persegi panjang adalah:", luas)

def hitung_luas_segitiga():
    alas = float(input("Masukkan panjang alas segitiga: "))
    tinggi = float(input("Masukkan tinggi segitiga: "))
    luas = 0.5 * alas * tinggi
    return luas

def hitung_luas_lingkaran(jari_jari):
    luas = 3.14 * jari_jari * jari_jari
    return luas

print("Menu pilihan:")
print("1. Menghitung luas bujur sangkar")
print("2. Menghitung luas persegi panjang")
print("3. Menghitung luas segitiga")
print("4. Menghitung luas lingkaran")

pilihan = input("Masukan pilihan anda: ")

if pilihan == '1':
    hitung_luas_bujur_sangkar()
elif pilihan == '2':
    hitung_luas_persegi_panjang()
elif pilihan == '3':
    luas_segitiga = hitung_luas_segitiga()
    print("Luas segitiga adalah:", luas_segitiga)
elif pilihan == '4':
    jari_jari = float(input("Masukkan panjang jari-jari lingkaran: "))
    luas_lingkaran = hitung_luas_lingkaran(jari_jari)
    print("Luas lingkaran adalah:", luas_lingkaran)
else:
    print("Pilihan tidak valid. Silakan masukkan pilihan 1, 2, 3, atau 4.")

# Contoh output:
# Menu pilihan:
# 1. Menghitung luas bujur sangkar
# 2. Menghitung luas persegi panjang
# 3. Menghitung luas segitiga
# 4. Menghitung luas lingkaran
# Masukan pilihan anda: 1