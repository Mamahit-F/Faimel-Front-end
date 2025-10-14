class Manusia:
    def __init__(self, nama):
        self.nama = nama
    
    def get_nama(self):
        return self.nama

    def set_nama(self, nama):
        self.nama = nama

class Mahasiswa(Manusia):
    def __init__(self, self, nama, jurusan):
        super().__init__(nama)
        self.jurusan = jurusan

    def get_jurusan(self):
        return self.jurusan

mahasiswa = Mahasiswa ("Semmy Taju", "Informatika")

print("INFORMASI AAWAS YANG DINPUTKAN:")
print("Nama: ", mahasiswa.get_nama())
print("Jurusan:", mahasiswa.get_jurusan())

mahasiswa.set_nama("Albert Toda")
mahasiswa.set_jurusan("Sistem Informasi")

print("\nSETELAH PERUBAHAN INFORMASI:")
print("Nama:", mahasiswa.get_nama())
print("Jurusan:")