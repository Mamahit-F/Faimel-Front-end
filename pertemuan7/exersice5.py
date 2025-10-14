# 1
# Buatlah program untuk mengkonversi suhu dari fahrenheit ke celcius
# Tampilkan dengan contoh format : 99.20 Fahrenheit = 37.33 Celcius
# Buat pseudocode & code program

# PSEUDOCODE
# SET fahrenheit <- 99.20
# CALCULATE celcius <- (fahrenheit-32) * 5/9
# DISPLAY celcius
# CODE
fahrenheit = 99.20
celcius = (fahrenheit-32) * 5/9
print("%.2f Fahrenheit = %.2f Celcius" % (fahrenheit, celcius))

#2
# No.2
# Buatlah program untuk menghitung BMI (Body Mass Index)
# Rumus : BMI = berat / (berat * tinggi), berat dalam kg dan tinggi dalam meter
# 170 cm = 1.7 m
# Tampilkan output dengan format:
# Tinggi: 1.7 meter, Berat: 96.2 Kg. BMI Anda adalah 33.3.
# Buat pseudocode & code program

#PSEUDOCODE
# SET tinggi = 1.7
# SET berat = 96.2
# CALCULATE BMI = berat/(tinggi**2)
# DISPLAY BMI
#CODE
tinggi = 1.7
berat = 96.2
BMI = berat/tinggi**2
print("Tinggi: %.1f meter, Berat: %.1f Kg. BMI Anda adalah %.1f." % (tinggi, berat, BMI))

