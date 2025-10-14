class Perpustakaan:
    def __init__(self):
        self.__nama = ""
        self.__jumlah_buku = 0

    def set_nama(self, nama):
        self.__nama = nama
    
    def get_nama(self):
        