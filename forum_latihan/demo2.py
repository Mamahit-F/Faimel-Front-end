class Produk():
    # variable
    jumlah_produk = 0

    # method constructor (default method)
    def __init__(self, nama, harga, tanggal_kedaluwarsa, negara_asal):
        self.nama = nama;
        self.harga = harga;
        self.tanggal_kedaluwarsa = tanggal_kedaluwarsa
        self.negara_asal = negara_asal

    # method 1
    def view_jum_produk(self, jumlah):
        Produk.jumlah_produk = jumlah;
        print('Total Produk: ', Produk.jumlah_produk);

    # method 2
    def detail_produk(self):
        print("Nama : ", self.nama);
        print("Harga: ", self.harga);

    def tampil_expire(self):
        return f"Expired date: {self.tanggal_kedaluwarsa}"

    def tampil_negara_asal(self):
        return f"Made in {self.negara_asal}"

# membuat objek pertama (Object isnstantiation)
produk1 = Produk('Tempe', 15000, '2027-02-18', 'Indonesia')

# membuat objek kedua (Object instantioation)
produk2 = Produk("Nutrisari", 5000, "2027-07-19", "Indonesia")

# membuat objek ketiga (Object instantioation)
produk3 = Produk("Mie_gori", 27000, "2027-05-07", "Indonesia")

# mengakses atrribut objek (Accessing class attributes)
produk1.detail_produk()
produk1.view_jum_produk(5)
print("Jumlah produk adalah {}".format(produk1.__class__.jumlah_produk));
print("Nama produk adalah {}".format(produk1.nama))
print(produk1.tampil_expire())
print(produk1.tampil_negara_asal())
print()

produk2.detail_produk()
produk2.view_jum_produk(10)
print("Jumlah produk adalah {}".format(produk2.__class__.jumlah_produk));
print(produk2.tampil_expire())
print(produk2.tampil_negara_asal())
print()

produk3.detail_produk()
produk3.view_jum_produk(15)
print("Jumlah produk adalah {}".format(produk3.__class__.jumlah_produk));
print("Nama produk adalah {}".format(produk3.nama))
print(produk3.tampil_expire())
print(produk3.tampil_negara_asal())