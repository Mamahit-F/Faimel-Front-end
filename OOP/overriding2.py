class Buah:
    def __init__(self, nama, harga, stok):
        self.nama = nama
        self.harga = harga
        self.stok = stok

    def beli(self, jumlah):
        if jumlah <= self.stok:
            self.stok -= jumlah
            return self.harga * jumlah
        else:
            return 0 

    def tambah_stok(self, jumlah):
        self.stok += jumlah

    def get_nama(self):
        return self.nama

    def get_harga(self):
        return self.harga

    def get_stok(self):
        return self.stok

    def get_info(self):
        return f"{self.nama}, harga: {self.harga}, stok: {self.stok}"

class Customer:
    def __init__(self, nama, saldo):
        self.nama = nama
        self.saldo = saldo

    def beli(self, buah, jumlah):
        total_harga = buah.beli(jumlah)
        if total_harga > 0  and self.saldo >= total_harga:
            self.saldo -= total_harga
            return f"{self.nama} membeli {jumlah} {buah.get_nama()} dengan harga {total_harga}"
        elif total_harga == 0:
            return f"Maaf, {buah.get_nama()} sedang kosong"
        else:
            return f"Maaf, saldo anda tidak mencukupi"

    def topup(self, jumlah):
        self.saldo += jumlah

    def get_saldo(self):
        return self.saldo

    def get_info(self):
        return f"{self.nama} saldo: {self.saldo}"

    def __str__(self):*
        return f"{self.nama}"

if __name__ == '__main__':
     apel = Buah('apel', 5000, 10)
     mangga = Buah('mangga', 7000, 5)
     john = Customer('John', 5000)
     semmy = Customer('semmy', 10000)

     print(apel.get_harga())
     print(mangga.get_info())

     print(john.beli(apel, 3))
     print(john.get_info())
     print(apel.get_info())

     print(john.beli(mangga, 10))
     print(john.get_info())
     print(mangga.get_info())

     john.topup(100000)
     print(john.get_info())

     print(john.beli(apel, 5))
     print(john.get_info())
     print(apel.get_info())

     print(john.beli(mangga, 2))
     print(john.get_info())
     print(mangga.get_info())

     print(semmy.beli(apel, 3))
     print(semmy.get_info())
     print(apel.get_info())

     print(semmy.beli(mangga, 10))
     print(semmy.get_info())
     print(mangga.get_info())

     print(semmy.get_info())

     print(semmy.beli(apel, 5))
     print(semmy.get_info())
     print(apel.get_info())

     print(semmy.beli(mangga, 2))
     print(semmy.get_info())
     print(mangga.get_info())