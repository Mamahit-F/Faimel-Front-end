# Assignment operator (=)
# Assignment operator adalah operator yang digunakan untuk memberi nilai pada sebuah variabel

# Ada 3 cara memberi nilai pada sebuah variabel:
# 1. Memberi nilai secara langsung

# phi = 3.14
# a = 10
# b = 20

# 2. Memberi nilai dari variabel yang lain
# a = 30
# a = b
# hasil = a + b
# print(a)

# 3. Memberi nilai daei inpur user
# nama = input ("Masukan nama anda :")
# print("Hello %s nice to meet you"%nama)

# angka1 = int (input ("Masukan angka 1: "))
# angka2 = int (input ("Masukan angka 2: "))
# result = angka1 + angka2
# print(result)

fahrenheit = float (input ("Masukan suhu dalam fahreneit: "))
celsius = (fahrenheit - 32) * (5/9)
print(f"{fahrenheit:.2f} Fahrenheit = {celsius:.2f} Celsius")


