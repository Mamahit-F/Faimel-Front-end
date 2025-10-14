# buatlah program dimana memiliki 2 fungsi yang dapat menghitung  . Menghitung body mass index (BMI). 
# Fungsi ini menerima 2 input yaitu berat (kg) dan tinggi (cm) namun tanpa return value (Fungsi bentuk 2). 
# Dimana fungsi ini akan menghitung BMI dan akan menampilkan output apalah BMI tersebut tergolong 
# kurus, normal, overweight atau obesitas, berdasarkan kondisi sesuai table dibawah ini

# BMI = berat (kg) / (tinggi (m))**2
# status                     range
# kurus                       <18.5
# normal                      18.5-24.9
# overweight                  25-29.9
# obesitas                    =>30

def hitungBMI(berat, tinggi):
    tinggi = tinggi / 100 
    bmi = berat / (tinggi ** 2)

    print("Nilai BMI: %.2f" % bmi)

    if bmi < 18.5:
        print("Status: Kurus")
    elif 18.5 <= bmi <= 24.9:
        print("Status: Normal")
    elif 25 <= bmi <= 29.9:
        print("Status: Overweight")
    else:
        print("Status: Obesitas")

# berat_badan = float(input("Masukkan berat badan (kg): "))
# tinggi_badan = float(input("Masukkan tinggi badan (cm): "))

# hitungBMI(berat_badan, tinggi_badan)

# menghitung berat badan ideal. fungsi ini menerima 2 input yaitu jenis kelamin dan tinggi dan memiliki return value berupa
# berat badan ideal (kg) (fungsi bentuk 4)
# rumus BMI:
# BMI = berat (kg) / (tinggi (m))**2
# status                     range
# kurus                       <18.5
# normal                      18.5-24.9
# overweight                  25-29.9
# obesitas                    =>30

# rumus broca untuk menghitung value berupa berat badan ideal:
# Pria: berat badan ideal (kg) = [tinggi badan (cm) - 100] - [(tinggi badan (cm) - 100) x 10 persen]
# wanita: berat badan ideal (kg) = [tinggi badan (cm) - 100] - [(tinggi badan (cm) - 100) x 15 persen]
# contoh output:
# 1. Laki-laki
# 2. Wanita
# Masukan jenis kelamin 1 atau 2: 1
# Masukan berat (kg): 92.2
# Masukan tinggi (cm): 177

# BMI anda : 29.43 (overweight)
# Berat badan ideal anda menurut rumus broca: 69.30

def hitung_bmi(berat, tinggi_cm):
    tinggi_m = tinggi_cm / 100  # Konversi tinggi dari cm ke m
    bmi = berat / (tinggi_m ** 2)

    print(f"\nBMI anda : {bmi:.2f}")

    if bmi < 18.5:
        print("Status: Kurus")
    elif 18.5 <= bmi <= 24.9:
        print("Status: Normal")
    elif 25 <= bmi <= 29.9:
        print("Status: Overweight")
    else:
        print("Status: Obesitas")

def hitung_berat_badan_ideal(jenis_kelamin, tinggi_cm):
    if jenis_kelamin == 1:  # Laki-laki
        persentase_pengurangan = 10
    elif jenis_kelamin == 2:  # Wanita
        persentase_pengurangan = 15
    else:
        print("Jenis kelamin tidak valid.")
        return

    berat_ideal = (tinggi_cm - 100) - ((tinggi_cm - 100) * (persentase_pengurangan / 100))
    print(f"Berat badan ideal anda menurut rumus Broca: {berat_ideal:.2f}")

berat_badan_bmi = float(input("Masukkan berat badan (kg): "))
tinggi_badan_bmi = float(input("Masukkan tinggi badan (cm): "))

hitung_bmi(berat_badan_bmi, tinggi_badan_bmi)

print("\n1. Laki-laki\n2. Wanita")
jenis_kelamin_bb = int(input("Masukkan jenis kelamin 1 atau 2: "))
tinggi_badan_bb = float(input("Masukkan tinggi badan (cm): "))

hitung_berat_badan_ideal(jenis_kelamin_bb, tinggi_badan_bb)


