# Input umur pengguna
umur = int(input("Masukkan umur Anda: "))

# Cek apakah pengguna di atas 18 tahun
if umur > 18:
    status_kerja = input("Apakah Anda sudah bekerja? (YA/TIDAK): ")
    
    # Jika sudah bekerja, hitung biaya hidup keluarga
    if status_kerja == "YA":
        pendapatan_bulanan = float(input("Masukkan pendapatan bulanan Anda: "))
        jumlah_tanggungan = int(input("Masukkan jumlah tanggungan Anda: "))
        biaya_hidup_keluarga = pendapatan_bulanan / jumlah_tanggungan
        
        # Tentukan status kategori berdasarkan biaya hidup keluarga
        if biaya_hidup_keluarga < 300000:
            status_kategori = "Penduduk Miskin"
        else:
            status_kategori = "Tidak Miskin"
    else:
        status_kategori = "Penduduk Miskin karena tidak bekerja"
else:
    status_sekolah = input("Apakah Anda masih bersekolah? (YA/TIDAK): ")
    
    # Tentukan status kategori berdasarkan status sekolah
    if status_sekolah == "YA":
        status_kategori = "Tidak Miskin"
    else:
        status_kategori = "Penduduk Miskin"

# Tampilkan hasil kategori
print("Anda terkategori sebagai:", status_kategori)
