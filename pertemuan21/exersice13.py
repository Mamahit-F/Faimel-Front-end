# Exersice 13
# Author      : Holy Faimel Mamahit
# Date        : 31 oktober 2023

def bujurSangkar ():
    sisi = float(input("masukan panjanng sisi bujur sangkar: "))
    luas = sisi * sisi
    print("Luas bujur sangkar adalah: %.2f" % luas)

def persegiPanjang(panjang, lebar):
    luas = panjang * lebar
    print("luas persegi panjang adala: %.2f" % luas)

def luasSegitiga():
    alas = float(input("masukan alas luas segitiga:"))
    tinggi = float(input("masukan tinggi luas segi tiga:"))
    luas = 1/2 * alas * tinggi
    return luas

def luasLinggkaran(jari2):
    luas = 3.14 * jari2**2
    return luas

print("Menu pilihan:")
print("1. Menghitung luas bujur sangkar")
print("2. Menghitung luas persegi panjang")
print("3. Menghitung luas segitiga")
print("4. Menghitung luas lingkaran")

pilihan = input("Masukan pilihan anda: ")

if pilihan == '1':
    bujurSangkar()
elif pilihan == '2':
    panjang = float(input("masukan panjang persegi panjang:"))
    lebar = float(input("masukan lebar persegi panjang:"))
    persegiPanjang(panjang, lebar)
elif pilihan == '3':
    output = luasSegitiga()
    print("Luas segitiga adalah: %.2f" % output)
elif pilihan =='4':
    jari2 = int(input("masukan jari jari lingkaran: "))
    output = luasLinggkaran(jari2)
    print("Luas linggkaran adalah : %.2f" % output)