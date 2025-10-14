# Exersice 10
# # Author     : Kelompok RIO:
#                             Faith
#                             Jechris 
#                             Jeiner
#                             Ralf
#                             Greefine
#                             Holy
# Date         : 3 oktober 2023
# --------------------------------------------------------------------
umur = int(input("Masukkan umur anda:"))
if umur >= 18:
    statusBekerja = str(input("Masukkan status bekerja anda. \"Bekerja\" atau \"Tidak Bekerja\" :"))
    if statusBekerja == "Bekerja":
        Pendapatan_Per_Bulan = int(input("Masukkan Pendapatan per bulan anda dengan format angka saja. contoh \"2000000\" :"))
        jumlahTanggungan = int(input("Masukkan jumlah tanggungan anda:"))
        biayaHidup = Pendapatan_Per_Bulan/jumlahTanggungan
        if biayaHidup < 300000:
            print ("=========================\nAnda masuk kategori penduduk miskin")
        else:
            print ("=========================\nAnda masuk kategori bukan penduduk miskin")
    elif statusBekerja == "Tidak Bekerja":
        print ("=========================\nAnda masuk kategori penduduk miskin")
    else:
        print ("Mohon isi status bekerja dengan benar. \"Bekerja\" atau \"Tidak Bekerja\"")
elif umur < 18:
    statusSekolah = str(input("Apakah anda masih sekolah? Jawab dengan format \"Ya\"/\"Tidak\" :"))
    if statusSekolah == "Ya":
        print ("=========================\nAnda masuk kategori bukan penduduk miskin")
    elif statusSekolah == "Tidak":
        print ("=========================\nAnda masuk kategori penduduk miskin")
    else:
        print ("Mohon isi status sekolah dengan benar. \"Ya\"/\"Tidak\"")
else:
    print ("Mohon isi usia anda dengan benar. Contoh 18 atau 14")
