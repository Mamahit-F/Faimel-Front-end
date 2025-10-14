class Produk():
    # class variable
    jumlah_produk = 0

    # constructor method
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga
        self.tanggal_kedaluwarsa = None
        self.negara_asal = None
        Produk.jumlah_produk += 1

    # method untuk menampilkan jumlah produk
    def view_jum_produk(self, jumlah):
        Produk.jumlah_produk = jumlah
        print('Total Produk:', Produk.jumlah_produk)

    # method untuk menampilkan detail produk
    def detail_produk(self):
        print("Nama :", self.nama)
        print("Harga:", self.harga)

    # method untuk menampilkan tanggal kedaluwarsa
    def tampil_expire(self):
        return f"Expired date: {self.tanggal_kedaluwarsa}" if self.tanggal_kedaluwarsa else "Tanggal kedaluwarsa belum ditentukan."

    # method untuk menampilkan negara asal
    def tampil_negara_asal(self):
        return f"Made in {self.negara_asal}" if self.negara_asal else "Negara asal belum ditentukan."


# membuat objek pertama (objek instantiation)
produk1 = Produk('Kerupuk', 5000)

# membuat objek kedua (objek instantiation)
produk2 = Produk('Taro', 3000)

# membuat objek ketiga (objek instantiation)
produk3 = Produk('Astor', 4000)

# mengakses atribut objek
produk1.detail_produk()
produk1.view_jum_produk(5)
print("Jumlah produk adalah {}".format(produk1.__class__.jumlah_produk))
print("Nama produk adalah {}".format(produk1.nama))
print(produk1.tampil_expire())
print(produk1.tampil_negara_asal())

produk2.detail_produk()
produk2.view_jum_produk(10)
print("Jumlah produk adalah {}".format(produk2.__class__.jumlah_produk))
print("Nama produk adalah {}".format(produk2.nama))
print(produk2.tampil_expire())
print(produk2.tampil_negara_asal())

produk3.detail_produk()
produk3.view_jum_produk(15)
print("Jumlah produk adalah {}".format(produk3.__class__.jumlah_produk))
print("Nama produk adalah {}".format(produk3.nama))
print(produk3.tampil_expire())
print(produk3.tampil_negara_asal())