# exerisce 9
# Author   : Holy Faimel Mamahit
# Date     : 26 september 2023
# ---------------------------------------------------

nilai = int(input("Masukan nilai: "))
if nilai >=0 and nilai <=39:
    print("F")
    print("Nilai bobot 0")
elif nilai >=40 and nilai <=59:
    print("D")
    print("Nilai bobot 1.0")
elif nilai >=60 and nilai <=66:
    print("C-")
    print("Nilai bobot 1.67")
elif nilai >=67 and nilai <=69:
    print("C")
    print("Nilai bobot 2.0")
elif nilai >=70 and nilai <=74:
    print("C+")
    print("Nilai bobot 2.33")
elif nilai >=75 and nilai <=77:
    print ("B-")
    print("Nilai bobot 2.67")
elif nilai >=78 and nilai <=81:
    print("B")
    print("Nilai bobot 3.0")
elif nilai >=82 and nilai <=84:
    print("B+")
    print("Nilai bobot 3.33")
elif nilai >=85 and nilai <=90:
    print("A-")
    print("Nilai bobot 3.67")
elif nilai >=91 and nilai <=100:
    print("A")
    print("Nilai bobot 4.0")
else:
   print ("Masukan nilai yang benar")