# Looping / pengulangan
# Instruksi kode program yang dieksekusi berulang kali

# Tipe looping
# 1. while Loop   : pengulangan yang dilakukan selama kondisi masih true
# 2. for loop     : eksekusi terhadap blok kdoe dilakukan berulang kali 
#                   sesuai dengan variabel yang mengatur pengulangan     
# 3. nested loop  : kombinasi pengulangan didalam pengulangan

# 1. WHILE LOOP
# -------------

# Tampilkan angka dari 1 sampai 10
# i = 1
# while i<= 10:
#     print(i)
#     i=i+1

# Tampilkan bilangan genap 1 - 100
# i = 2
# while i<= 100:
#     print(i)
#     i+=2


# Buatlah tabel perkalian sampai 10 dari angka yang dimasukan
# masukan angka 5
angka = int(input("Masukan angaka: "))
i = 1
while i<=10:
    print("%d x %d = %d" % (i, angka, i*angka))
    i = i + 1
