# Exersice 7
# Author   : Kelompok RIO
# Date     : 14 September 2023
# -----------------------------------------------------

# Name : Holy Faimel Mamahit
# PSEUDOCODE
# SPHERE
# 1. INPUT r
# 2. INPUT phi <- 3.14
# 3. CALCULATE volume <- (4/3) * phi * (r**3)
# 4. DISPLAY volume
r = float(input("Masukan nilai r: "))
phi = 3.14
volume = (4/3) * phi * (r**3)
result = ("Volume sphere = %.2f" % volume)
print(result)

# Name : Ralf Abas
# Menghitung Volume cube
# Rumus = a**3
# PSEUDOCODE
# 1. INPUT a
# 2. CALCULATE volume <- a**3
# 3. DISPLAY volume
a = float(input("masukkan nilai a : "))
volume = a**3 
result = ("Volume cube = %.2f" % volume)
print(result)

# Name : Grifin
# Menghitung Volume RC Cylinder
# Rumus = phi * r**2 * h
# PSEUDOCODE
# 1. INPUT r
# 2. INPUT h
# 3. INPUT phi <- 3.14
# 4. CALCULATE volume <- phi * r**2 * h
# 5. DISPLAY volume
phi = 3.14
r = float(input("masukkan nilai r : "))
h = float(input("masukkan nilai h : "))
volume = phi * r**2 * h
result = ("Voleme RC Cylinder =%.2f " % volume)
print(result)

# Name : Faith
# Right Circular Cone
# Rumus: Volume = 1/3 x phi x r^2 x h
# PSEUDOCODE
# 1. INPUT r
# 2. INPUT h
# 3. INPUT phi <- 3.14
# 4. CALCULATE volume <- (1/3)phi(r**2)*h
# 5. DISPLAY volume
r = int(input("Masukkan jari-jari kerucut:"))
h = int(input("Masukkan tinggi kerucut:"))
phi = 3.14
volume = (1/3)*phi*(r**2)*h
print("Volume kerucut tersebut adalah: %.2f" % volume)

# Name : jeiner
# Menghitung Volume Hemisphere
# Rumus = (2/3) * phi * r**3
# PSEUDOCODE
# 1. INPUT r
# 2. INPUT phi <- 3.14
# 3. CALCULATE volume <- (2/3) * phi * r**3
# 4. DISPLAY volume
# phi = 3.14
r = float(input("masukkan nilai r : "))
volume = (2/3) * phi * r**3
result = ("Volume Hemisphere = %.2f" % volume)
print(result)

# Name : jei
# Menghitung Volume cuboid
# Rumus = l * b * h 
# PSEUDOCODE
# 1. INPUT l
# 2. INPUT b
# 3. INPUT h
# 4. CALCULATE volume <- l * b * h 
# 5. DISPLAY Volume
l = float(input("masukkan nilai l : "))
b = float(input("masukkan nilai b : "))
h = float(input("masukkan nilai h : "))
volume = l * b * h 
result = ("Volume cuboid = %.2f" % volume)
print(volume)