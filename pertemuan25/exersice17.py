# Exersice 17
# Date     : 21 november 2023
# Author   : Holy Faimel Mamahit
# --------------------------------------
def input_nilai():
    nilai = []
    for i in range(5):
        angka = float(input("Masukkan angka %d: " % (i + 1)))
        nilai.append(angka)
    return nilai

def hitung_rata_rata(nilai):
    total = sum(nilai)
    jumlah_nilai = len(nilai)
    if jumlah_nilai > 0:
        return total / jumlah_nilai
    else:
        return None

def tampilkan_statistik_nilai(nilai):
    rata_rata = hitung_rata_rata(nilai)
    if rata_rata is not None:
        print("Nilai rata-rata: %.2f" % rata_rata)
        print("Nilai terkecil:", min(nilai))
        print("Nilai terbesar:", max(nilai))
        
    else:
        print("Input dengan benar.")
    
x=0
while x+1:
    nilai1 = input_nilai()
    tampilkan_statistik_nilai(nilai1)

    nilai2 = input_nilai()
    tampilkan_statistik_nilai(nilai2)

    nilai3 = input_nilai()
    tampilkan_statistik_nilai(nilai3)

    nilai4 = input_nilai()
    tampilkan_statistik_nilai(nilai4)
