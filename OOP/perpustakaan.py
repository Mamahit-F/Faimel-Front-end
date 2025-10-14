class Perpustakaan:
    def __init__(self, nama_perpustakaan, alamat, jumlah_koleksi_buku, buku_terpinjam, denda_per_hari):
        self._nama_perpustakaan = nama_perpustakaan
        self._alamat = alamat
        self._jumlah_koleksi_buku = jumlah_koleksi_buku
        self._buku_terpinjam = buku_terpinjam
        self._denda_per_hari = denda_per_hari

    def get_nama_perpustakaan(self):
        return self._nama_perpustakaan

    def set_nama_perpustakaan(self, nama_perpustakaan):
        self._nama_perpustakaan = nama_perpustakaan

    def get_alamat(self):
        return self._alamat

    def set_alamat(self, alamat):
        self._alamat = alamat

    def get_jumlah_koleksi_buku(self):
        return self._jumlah_koleksi_buku

    def set_jumlah_koleksi_buku(self, jumlah_koleksi_buku):
        self._jumlah_koleksi_buku = jumlah_koleksi_buku

    def get_buku_terpinjam(self):
        return self._buku_terpinjam

    def set_buku_terpinjam(self, buku_terpinjam):
        self._buku_terpinjam = buku_terpinjam

    def get_denda_per_hari(self):
        return self._denda_per_hari

    def set_denda_per_hari(self, denda_per_hari):
        self._denda_per_hari = denda_per_hari

    def informasi_perpustakaan(self):
        return f"Perpustakaan {self._nama_perpustakaan}, Alamat: {self._alamat}, Total Koleksi: {self._jumlah_koleksi_buku} buku, Buku Terpinjam: {self._buku_terpinjam}, Denda Per Hari: Rp. {self._denda_per_hari}"

    def tambah_buku(self, jumlah):
        self._jumlah_koleksi_buku += jumlah

    def pinjam_buku(self, jumlah):
        if self._jumlah_koleksi_buku >= jumlah:
            self._buku_terpinjam += jumlah
            self._jumlah_koleksi_buku -= jumlah
            return True
        else:
            return False

    def kembalikan_buku(self, jumlah):
        if self._buku_terpinjam >= jumlah:
            self._buku_terpinjam -= jumlah
            self._jumlah_koleksi_buku += jumlah
            return True
        else:
            return False

    def jumlah_buku_tersedia(self):
        return self._jumlah_koleksi_buku

    def jumlah_buku_dipinjam(self):
        return self._buku_terpinjam


# Membuat objek perpustakaan
perpustakaan = Perpustakaan("Universitas Gajah Mada", "Jl. Diponegoro No. 123", 900, 500, 1000)

# Melakukan 10 operasi yang berbeda
perpustakaan.set_nama_perpustakaan("Universitas Indonesia")
perpustakaan.set_alamat("Jl. Soekarno No. 345")
perpustakaan.set_denda_per_hari(2000)
perpustakaan.tambah_buku(440)
perpustakaan.pinjam_buku(350)
perpustakaan.kembalikan_buku(30)
tersedia = perpustakaan.jumlah_buku_tersedia()
dipinjam = perpustakaan.jumlah_buku_dipinjam()
info_perpustakaan = perpustakaan.informasi_perpustakaan()

# Mencetak informasi tentang perpustakaan
print(info_perpustakaan)
print("Jumlah buku tersedia:", tersedia)
print("Jumlah buku dipinjam:", dipinjam)