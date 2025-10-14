def hitung_rata_rata(arr):
    total = 0
    for nilai in arr:
        total += nilai
    rata_rata = total / len(arr)
    return rata_rata
# total diinisialisasi ke nilai 0. Ini akan digunakan untuk menyimpan jumlah semua nilai di dalam array.
# Kita menggunakan loop for untuk mengiterasi melalui setiap nilai dalam array arr.
# Setiap nilai ditambahkan ke total.
# Setelah selesai menghitung total, kita bagi total dengan panjang array (len(arr)) untuk mendapatkan rata-rata.
# Nilai rata-rata dikembalikan oleh fungsi.

n = int(input("Masukkan jumlah nilai: "))
# Fungsi input() digunakan untuk menerima input dari pengguna dalam bentuk string.
# Kita menggunakan int() untuk mengonversi string tersebut menjadi bilangan bulat, 
# karena kita ingin menghitung jumlah nilai yang akan dimasukkan.

nilai = []
for i in range(n):
    nilai.append(float(input("Masukkan nilai ke-{}: ".format(i + 1))))
# Kita inisialisasi sebuah array kosong nilai.
# Kita menggunakan loop for untuk mengulang sebanyak n kali, dimana n adalah jumlah nilai yang telah dimasukkan pengguna sebelumnya.
# Dalam setiap iterasi, kita meminta pengguna untuk memasukkan nilai menggunakan input().
# Kita menggunakan float() untuk mengonversi input pengguna ke tipe data float, karena kita ingin menerima input dalam bentuk angka desimal.
# Nilai tersebut kemudian ditambahkan ke array nilai menggunakan metode append().

rata_rata_nilai = hitung_rata_rata(nilai)
# Kita menyimpan hasil rata-rata yang dikembalikan oleh fungsi hitung_rata_rata ke dalam variabel rata_rata_nilai.

print("Rata-rata nilai adalah:", rata_rata_nilai)
# Hasil rata-rata tersebut dicetak ke layar bersama dengan pesan yang sesuai.