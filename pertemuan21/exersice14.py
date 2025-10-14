# Exersice 14
# Name       : Holy faimel mamahit
# date       : 1 November 2023
# ================================================================
def luasVolumeTabung():
    jari2 = float(input("Masukan jari jari tabung: "))
    tinggi = float(input("Masukan tinggi tabung: "))
    luas = 2 * 3.14 * jari2 * (jari2 + tinggi)
    volume = 3.14 * jari2**2 * tinggi
    print("Luas tabung adalah: %.2f" % luas) 
    print("Volume tabung adalah: %.2f" % volume)

def luasVolumeKubus(sisi):
    luas = 6 * sisi**2
    volume = sisi**3
    print("Luas kubus adalah: %.2f" % luas)
    print("Volume kubus adalah: %.2f" % volume)

def luasVolumeBalok():
    panjang = float(input("Masukan panjang balok: "))
    lebar = float(input("Masukan lebar balok: "))
    tinggi = float(input("Masukan tinggi balok: "))
    luas = 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)
    volume = panjang * lebar * tinggi
    return luas, volume

def luasVolumeBola(jari2):
    luas = 4 * 3.14 * jari2**2
    volume = 4/3 * 3.14 * jari2**3
    return luas, volume

print("Program Menghitung Luas dan Volume Bangun Ruang")
print("1. Tabung")
print("2. Kubus")
print("3. Balok")
print("4. Bola")

pilihan = input("Masukan pilihan anda: ")

if pilihan == '1':
    luasVolumeTabung()
elif pilihan == '2':
    sisi = float(input("Masukan sisi kubus: "))
    luasVolumeKubus(sisi)
elif pilihan == '3':
    output = luas, volume = luasVolumeBalok()
    print("Luas balok adalah : %.2f" % luas)
    print("Volume tabung adalah: %.2f" % volume)
elif pilihan == '4':
    jari2 = float(input("Masukan jari jari bola: "))
    output = luas, volume = luasVolumeBola(jari2)
    print("Luas bola adalah: %.2f" % luas)
    print("Volume bola adalah: %.2f" % volume)  
else:
    print("Tolong masukan pilihan yang benar")