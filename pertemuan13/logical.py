# operator logika

# And, Or, Not

# Tabel kebenara And
# True And True  = True
# True And False = False
# False And True = False
# False And True = False
print (True and True)
print (True and False)
print (False and True)
print (False and False)

a = 7
print(a > 5 and a < 10)

b = 10
print (b >=5 and b <= 20)
print (b < 15 and b >= 25)

# Tabel kebenaran Or
# True Or True   =
# True Or False  =
# False Or True  =
# False Or False =
 


# Tabel kebenaran Not
# Not True  = False
# Not False = True

print(True or False and True)
#      True    or   False
#             Turn

# Buat program jika umur lebih dari 17 tahun dan 
# Kurang dari 65 tahun tampilkan anda bisa buat SIM kendaraan 

# umur = str(input("Masukan umur anda: "))

# jika menggunakan AND
umur = 15
if umur >=17 and umur <=65 :
    print("Anda bisa buat SIM kendaraan bermotor")
else:
    print("Anda tidak bisa buat SIM kendaraan bermotor")

# jika menggunakan OR
if umur < 17 or umur > 65:
    print("Anda tidak bisa buat SIM kendaraan")
else:
    print("Anda bisa buat SIM kendaraan bermotor")

# jika suhu udara lebih kecil 36 derajat atau lebih besar 39 derajat
# tampilkan "Saya akan tidur dirumah"
# sebaliknya "Saya akan berolahraga diluar rumah"

suhu = 33
if suhu > 36 and suhu <= 39:
    print("Saya akan tidur dirumah")
else:
    print("saya akan berolahraga diluar rumah")