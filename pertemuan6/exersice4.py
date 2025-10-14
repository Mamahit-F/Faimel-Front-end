# buatlah pseudocode dan program untuk menghitung luas lingkaran 
# dimana jari-jari adalah 18. Tampilkan luas lingkaran
# dengan 2 angka dibelakang koma.

# pseudocode
# SET radius <- 18
# SET phi <- 3.14
# CALCULATE <- phi * radius ** 2
# DISPLAY luas 

radius = 18
phi = 3.14
luas = phi * radius ** 2

print("%.2f" % luas)