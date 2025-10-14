harga_pertalite = 7850
harga_pertamax = 9200
harga_pertamax_turbo = 12500
harga_dexlite = 9700

# Nilai tukar mata uang
nilai_tukar_usd = 14150
nilai_tukar_sgd = 10534
nilai_tukar_twd = 500
nilai_tukar_yen = 124

# Menu utama
while True:
    print("\nMenu Konversi:")
    print("1. Konversi BBM")
    print("2. Konversi Mata Uang")
    print("3. Keluar")

    pilihan = input("Pilih menu (1/2/3): ")

    if pilihan == "1":
        print("\nKonversi BBM:")
        print("BBM yang tersedia: Pertalite, Pertamax, Pertamax Turbo, Dexlite")
        jenis_bbm = input("Pilih jenis BBM: ")
        jumlah_liter = int(input("Masukkan jumlah liter (1-10): "))
        
        if 1 <= jumlah_liter <= 10:
            if jenis_bbm == "Pertalite":
                total_harga = jumlah_liter * harga_pertalite
            elif jenis_bbm == "Pertamax":
                total_harga = jumlah_liter * harga_pertamax
            elif jenis_bbm == "Pertamax Turbo":
                total_harga = jumlah_liter * harga_pertamax_turbo
            elif jenis_bbm == "Dexlite":
                total_harga = jumlah_liter * harga_dexlite
            else:
                print("Jenis BBM tidak valid")
                continue
            
            print(f"Total harga untuk {jumlah_liter} liter {jenis_bbm}: Rp. {total_harga}")
        else:
            print("Jumlah liter harus antara 1 hingga 10.")
    elif pilihan == "2":
        print("\nKonversi Mata Uang:")
        print("Mata uang yang tersedia: USD, SGD, TWD, Yen")
        mata_uang = input("Pilih mata uang: ")
        jumlah_rupiah = int(input("Masukkan jumlah Rupiah (5000-100000): "))
        
        if 5000 <= jumlah_rupiah <= 100000:
            if mata_uang == "USD":
                jumlah_mata_uang = jumlah_rupiah / nilai_tukar_usd
            elif mata_uang == "SGD":
                jumlah_mata_uang = jumlah_rupiah / nilai_tukar_sgd
            elif mata_uang == "TWD":
                jumlah_mata_uang = jumlah_rupiah / nilai_tukar_twd
            elif mata_uang == "Yen":
                jumlah_mata_uang = jumlah_rupiah / nilai_tukar_yen
            else:
                print("Mata uang tidak valid")
                continue
            
            print(f"{jumlah_rupiah} Rupiah setara dengan {jumlah_mata_uang:.2f} {mata_uang}")
        else:
            print("Jumlah Rupiah harus antara 5000 hingga 100000.")
    elif pilihan == "3":
        print("Terima kasih, program selesai.")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih 1, 2, atau 3.")