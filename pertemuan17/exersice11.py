# exersice 11
# Author    : Holy Faimel Mamahit
# Date      : 17 oktober 2023 
# -----------------------------
print("MENU KONVERSI")
print("-------------")
print("1. BBM")
print("2. Mata Uang")
pilihan = input("pilih menu 1/2: ")
if pilihan == "1":
    print("Konversi BBM")
    pertalite = 7850
    pertamax = 9200
    pertamax_turbo = 12500
    dexlite = 9700
    liter = 1
    while liter <=10:
        print(liter, "liter:")
        print("pertalite: Rp", liter * pertalite)
        print("Pertamax: Rp", liter * pertamax)
        print("Pertamax_turbo: Rp", liter * pertamax_turbo)
        print("Dexlite: Rp", liter * dexlite)
        liter +=1
elif pilihan == "2":
    USD = 14500
    SGD = 10534
    TWD = 500
    YEN = 124
    rupiah = 5000
    while rupiah <= 100000:
        print("USD: $%.2f" % (rupiah/USD))
        print("SGD: $%.2f" % (rupiah/SGD))
        print("TWD: NT$%.2f" % (rupiah/TWD))
        print("YEN: ¥%.2f" % (rupiah/YEN))
        rupiah += 5000
else:
    print("Mohon masukan pilihan yang benar")


