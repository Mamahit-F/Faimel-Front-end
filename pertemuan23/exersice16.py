def konversi_nilai_huruf(nilai_akhir):
    if nilai_akhir >= 91:
        return "A"
    elif nilai_akhir >= 85:
        return "A-"
    elif nilai_akhir >= 82:
        return "B+"
    elif nilai_akhir >= 78:
        return "B"
    elif nilai_akhir >= 75:
        return "B-"
    elif nilai_akhir >= 70:
        return "C+"
    elif nilai_akhir >= 67:
        return "C"
    elif nilai_akhir >= 60:
        return "C-"
    elif nilai_akhir >= 40:
        return "D"
    else:
        return "F"

jumlah_mahasiswa = int(input("Masukkan jumlah mahasiswa: "))

mahasiswa = []
for i in range(jumlah_mahasiswa):
    nama_mahasiswa = input(f"Nama mahasiswa {i + 1}: ")
    tugas = float(input("Nilai tugas: "))
    quiz = float(input("Nilai quiz: "))
    ujian_mid = float(input("Nilai ujian mid: "))
    ujian_final = float(input("Nilai ujian final: "))

    nilai_akhir = (tugas + quiz + ujian_mid + ujian_final) / 4
    nilai_huruf = konversi_nilai_huruf(nilai_akhir)

    mahasiswa.append((nama_mahasiswa, nilai_akhir, nilai_huruf))

print("\t")
print("***************************************************************")
print("Laporan Nilai %d Mahasiswa Mata Kuliah Computer Programming" % (i + 1))
print("***************************************************************")
for nama, nilai_akhir, nilai_huruf in mahasiswa:
    print(f"Nama mahasiswa: {nama}")
    print(f"Nilai akhir: {nilai_akhir:.2f}")
    print(f"Nilai huruf: {nilai_huruf}\n")