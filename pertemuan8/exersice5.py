# Exersice 5
# Author    :
# Date      : 
# -----------------------------

# 1. Program untuk konversi suhu dari fahrenheit ke celcius
# Rumus : celcius = (fahrenheit - 32) * (5/9)

#  Pseudocode
# 1. INPUT fahrenhait
# 2. CALCULATE celcius <- (fahrenhait - 32) * (5/9)
# DISPLAY celcius

fahrenhait = 99.20
celcius = (fahrenhait - 32) * (5/9)
print("%.2f fahrenhait = %.2f celcius" % (fahrenhait, celcius))

# 2. Program untuk menghitung BMI 
# Rumus : BMI = berat / (tinggi * tinggi  )

#  Pseudocode
# 1. INPUT berat
# 2. INPUT tinggi
# 3. CALCULATE BMI <- berat (tinggi * tinggi)
# DISPLAY BMI

berat = 96.2
tinggi = 1.7
bmi = berat /(tinggi * tinggi)
print("Tinggi: %.1f meter, berat: %.1f kg. BMI anda adalah %.1f %"(tinggi, berat, ))