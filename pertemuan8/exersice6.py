# Exersice 6
# Author      : Holy Faimel Mamahit
# Date        : 7 September 2023
# Menghitung luas dan volume tabunng


# 1.
# Pseudocode 
# INPUT Rumus luas <- (2 * phi * r * t)
# INPUT Rumus volume <- phi * r * t
# CALCULATE LUAS
# CALCULATE VOLUME
# DISPLAY Result

phi = 3.141593
r = float (input ("Masukan jari jari tabung: "))
t = float (input ("masukan tinggi tabung: "))
luas = 2 * r * t
volume = phi * r * t**2
print(luas)
print(volume)

# 2.
# PSEUDOCODE
# INPUT <- luas (2 * p * l) + (2 * p * t) + (2 * l * t)
# INPUT <- volume p * l * t
# CALTULATE Luas
# CALCULATE Volume
# DISPLAY Result

p = float (input ("Masukan nilai panjang: "))
l = float (input ("Masukan nilai lebar: "))
t = float (input ("Masukan nilai tinggi: ")) 
luas = (2 * p * l) + (2 * p * t) + (2 * l * t)
volume = p * l * t
print(luas)
print(volume)

# 3.
# PSEUDOCODE
# INPUT x = a**3 + b**2 + c
# INPUT a
# INPUT b
# INPUT c
# CALCULATE
# DISPLAY

a = int (input ("Masukan nilai a: "))
b = int (input ("Masukan nilai b: "))
c = int (input ("Masukkan nilai c: "))
x = a**3 + b**2 + c
result = ("x = %s" % x)
print(result)