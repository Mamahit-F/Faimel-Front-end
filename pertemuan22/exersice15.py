# Exersice 15
# Author  : Holy Faimel Mamahit
# Date    : 7 November 2023



# Buatlah program yang menerima 5 input dari user
# dan disimpan ke dalam list. Kemudian tampilkan 
# nilai rata-rata dan nilai terkecil serta terbesar dri angka yang dimasukan user  

nilai = []

for i in range(5):
    angka = float(input("Masukkan angka %d: " % (i + 1)))
    nilai.append(angka)

total = 0
for angka in nilai:
    total += angka

jumlah_nilai = len(nilai)
if jumlah_nilai > 0:
    rata2 = total / jumlah_nilai
    print("Nilai rata-rata: %.2f" % rata2)
else:
    print("Input dengan benar.")    