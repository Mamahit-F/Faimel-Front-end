class Penulis:
    def __init__(self, nama):
        self.nama = nama
        self.daftar_buku = []

    def tulis_buku(self, judul):
        buku = Buku(judul, self.nama)
        self.daftar_buku.append(buku)

class Buku:
    def __init__(self, judul, penulis):
        self.judul = judul
        self.penulis = penulis

penulis1 = Penulis("Semmy Taju")

penulis1.tulis_buku("Java Pemrograman")
penulis1.tulis_buku("Data structures in python")
penulis1.tulis_buku("Machine Learning Algoritms")

for buku in penulis1.daftar_buku:
    print("Judul Buku: ", buku.judul)
    print("Penulis buku: ", buku.penulis)
    print()


