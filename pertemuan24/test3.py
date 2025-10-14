def hitung_bmi(berat, tinggi_cm):
    tinggi_m = tinggi_cm / 100 
    bmi = berat / (tinggi_m ** 2)
    return bmi

def hitung_berat_badan_ideal(jenis_kelamin, tinggi_cm):
    if jenis_kelamin == 1: 
        persentase_pengurangan = 10
    elif jenis_kelamin == 2:
        persentase_pengurangan = 15
    else:
        print("Jenis kelamin tidak valid.")
        return

    berat_ideal = (tinggi_cm - 100) - ((tinggi_cm - 100) * (persentase_pengurangan / 100))
    return berat_ideal

print("1. Laki-laki\n2. Wanita")
jenis_kelamin = int(input("Masukan jenis kelamin 1 atau 2: "))
berat_badan = float(input("Masukan berat badan (kg): "))
tinggi_badan = float(input("Masukan tinggi badan (cm): "))

bmi = hitung_bmi(berat_badan, tinggi_badan)

print("Nilai BMI: %.2f" % bmi)

if bmi < 18.5:
        print("Status: Kurus")
elif 18.5 <= bmi <= 24.9:
        print("Status: Normal")
elif 25 <= bmi <= 29.9:
        print("Status: Overweight")
else:
        print("Status: Obesitas")

berat_ideal = hitung_berat_badan_ideal(jenis_kelamin, tinggi_badan)

if berat_ideal:
    print("Berat badan ideal anda menurut rumus Broca: %.2f " % berat_ideal)


