# Test_1
# Author    : Holy Faimel Mamahit
# Date      : 12 september 2023 
# -----------------------------

# a = float(input("Masukan panjang sisi tegak: "))
# b = float(input("Masukan panjang sisi alas: "))
# c = math.sqrt(a**2 + b**2)

# Soal 1.
# PSEUDOCODE
# 1. INPUT a
# 2. INPUT b 
# 3. CALCULATE c <- (a**2 + b**2)
# 4. DISPLAY C

a = float(input("Masukkan panjang sisi tegak: "))
b = float(input("Masukkan panjang sisi alas: "))
c = (a**2 + b**2)**1/2
print("Panjang sisi miring adalah: %.2f" % c,)


# Soal 2.
# PSEUDOCODE
# 1. INPUT g <- 9.81
# 2. INPUT h
# 3. CALCULATE t
# 4. DISPLAY t

g = 9.81
h = float(input("Masukkan tinggi jatuh: "))
t = (2 * h / g)**1/2
print("Waktu yang diperlukan untuk benda jatuh adalah: %.2f" % t, ("detik"))