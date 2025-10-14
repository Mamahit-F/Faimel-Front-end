# parent class
class GrandFather:

    nama = "Robert Todo"
    __max_umur = "60"

    def __init__(self, input_nama, input_umur):
        self.nama = input_nama
        self.__max_umur = input_umur
        self.__info()

    def menulis(self):
        print("Skill grandfather adalah menulis.")

    def __info(self):
        print("GrandFather:", self.nama, "dan umur:", self.__max_umur,",")

class Father(GrandFather):
    def membaca(self):
        print("Skill father adalah membaca jurnal internasional.")

    def menulis(self):
        print("Skill father adalah menulis jurnal internasional.")

    def programmer(self):
        print("Skill father adalah membuat program komputer.")

class Semmy(Father):
    def berenang(self):
        print("Skill Semmy adalah berenang.")

    def programmer(self):
        print("Skill Semmy adalah programmer Java.")

    def init(self, input_nama, input_umur):
        super().init(input_nama, input_umur)

class Buddy(Father):
    def pidato(self):
        print("Skill Buddy adalah pidato.")

    def menulis(self):
        print("Skill Buddy adalah menulis buku.")

    def init(self, input_nama, input_umur):
        super().init(input_nama, input_umur)

obj_sem = Semmy("Hendra Bayu", "58")
obj_sem.menulis()
obj_sem.membaca()
obj_sem.berenang()
obj_sem.programmer()

obj_buddy = Buddy("Buddy", "45")
obj_buddy.membaca()
obj_buddy.programmer()
obj_buddy.pidato()
obj_buddy.menulis()