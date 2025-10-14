# Exersice 12
# Author     : Holy Faimel Mamahit
# Date       : 24 oktober 2023

n = int(input("Masukkan jumlah angka: "))

angka_terbesar = -float("inf")
angka_terkecil = float("inf")
total = 0

for i in range(n):
    angka = float(input("Masukkan angka ke-" + str(i + 1) + ": "))
    
    if angka > angka_terbesar:
        angka_terbesar = angka
    if angka < angka_terkecil:
        angka_terkecil = angka

    total += angka

rata_rata = total / n
print("\t")
print("Nilai terbesar adalah: " + str(angka_terbesar))
print("Nilai terkecil adalah: " + str(angka_terkecil))
print("Nilai rata-rata adalah: " + str(rata_rata))