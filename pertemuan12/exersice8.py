# Exersice 8
# Author    : Holy Faimel Mamahit
# Date      : 21 september 2023
# --------------------------------------

# Soal no 1.
# PSEUDOCODE
# 1. INPUT nilai
# 2. if nilai >= 70
# 3.    DISPLAY lulus
# 3. else
# 4.    DISPLAY tidak lulus
nilai = int(input("Masukan nilai: "))
if nilai >= 70:
    print("Lulus")
else:
    print("Tidak lulus")

# Soal no 2.
# PSEUDOCODE
# 1. INPUT nama
# 2. INPUT jenis kelamin
# 3. IF jenis_kelamin == "pria"
# 4.    DISPLAY halo bro (nama)
# 5. IF jenis_kelamin == "wanita"
# 6.    DISPLAY halo sis (nama)
nama = str(input("Masukan nama: "))
jenis_kelamin = str(input("Masukan jenis kelamin:"))
if jenis_kelamin == "pria": 
    print("halo bro", nama)
if jenis_kelamin == "wanita":
    print("helo sis", nama)