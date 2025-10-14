# Mid test
# Author    : Holy Faimel Mamahit
# date      : 4 oktober 2023
# --------------------------------------------------

# Soal 1.
jumlah_orang = int(input("Masukkan jumlah teman (termasuk Budi): "))
harga_nasi_ayam_goreng = int(input("Masukkan harga satu porsi nasi ayam goreng: "))
harga_es_buah = int(input("Masukkan harga satu gelas es buah: "))
biaya_per_orang = harga_nasi_ayam_goreng + harga_es_buah
total_biaya = jumlah_orang * biaya_per_orang
print("Total uang yang harus dikeluarkan oleh Budi adalah Rp", total_biaya)

# Soal 2.
harga_mobil = int(input("Masukan harga mobil nyang dibeli bapak amir:"))
bayaran_awal = int(input("Masukan pembayaran awal:"))
cicilan = int(input("Masukan cicilan perbulan:"))
hutang_pak_amir = harga_mobil - bayaran_awal
sisa_bulan = hutang_pak_amir / cicilan

print("Hutang pak amir akan lunas dalam %d bulan" % sisa_bulan)

# soal 3. 

bilangan = input("Masukkan bilangan: ")
if bilangan:
    bilangan = float(bilangan)
    if bilangan == 0:
        print("Ini adalah bilangan nol.")
    elif bilangan % 1 == 0:
        print("Ini adalah bilangan bulat.")
    else:
        print("Ini adalah bilangan pecahan.")
else:
    print("Bilangan yang anda masukan tidak valid.")

# Soal 4.
angka_1 = float(input("Masukkan angka 1:"))
angka_2 = float(input("Masukkan angka 2:"))
angka_3 = float(input("Masukkan angka 3:"))
terbesar = angka_1
if angka_2 > terbesar:
    terbesar = angka_2
if angka_3 > terbesar:
    terbesar = angka_3
print("Angka yang terbesar adalah", terbesar)

# Soal 5.
pembelian = float(input("Masukkan jumlah pembelian (dalam Rupiah): "))
bonus = ""
if 100000 <= pembelian < 200000:
    bonus = "Diskon 5%"
elif 200000 <= pembelian < 300000:
    bonus = "Tiket ke Yogyakarta"
elif 300000 <= pembelian < 400000:
    bonus = "Tiket ke Bali"
elif 400000 <= pembelian <= 500000:
    bonus = "Jam tangan Rolex"
elif pembelian > 500000:
    bonus = "Tiket ke Swiss"

if bonus:
    print("Bonus yang anda dapatkan:", bonus)
else:
    print("Minimal nominal pembelian untuk mendapatakn bonus adalah Rp.100.000")