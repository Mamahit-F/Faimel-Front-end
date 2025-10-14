import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from google.colab import drive

# Menghubungkan Google Drive
try:
    drive.mount('/content/drive')
except Exception as e:
    print(f"Terjadi kesalahan saat menghubungkan ke Google Drive: {e}")

# Membaca dataset
try:
    data = pd.read_csv('/content/drive/My Drive/Classroom/Student_performance_data _.csv')
except FileNotFoundError:
    print("File tidak ditemukan. Pastikan path file sudah benar.")
except pd.errors.EmptyDataError:
    print("File kosong. Silakan periksa file CSV.")
except Exception as e:
    print(f"Terjadi kesalahan saat membaca file: {e}")

# 1. Ada berapa total students dalam dataset ini ?
try:
    total_students = data.shape[0]
    print(f"Total siswa: {total_students}")
except Exception as e:
    print(f"Terjadi kesalahan saat menghitung total siswa: {e}")

# 2. Ada umur berapa saja student dalam dataset ini ? Tampilkan total student per kategori umur
try:
    Age_distribution = data['Age'].value_counts().sort_index()
    print("\nDistribusi Umur Siswa:")
    print(Age_distribution)
except KeyError:
    print("Kolom 'Age' tidak ditemukan dalam dataset.")
except Exception as e:
    print(f"Terjadi kesalahan saat menghitung distribusi umur: {e}")

# 3. Etnis manakah yang terbanyak? Tampilkan jumlah student per kategori etnis
try:
    Ethnicity_distribution = data['Ethnicity'].value_counts()
    print("\nDistribusi Etnis Siswa:")
    print(Ethnicity_distribution)
except KeyError:
    print("Kolom 'Ethnicity' tidak ditemukan dalam dataset.")
except Exception as e:
    print(f"Terjadi kesalahan saat menghitung distribusi etnis: {e}")
    
# 4. Rata-rata GPA berdasarkan kategori pria dan wanita
try:
    gpa_by_gender = data.groupby('Gender')['GPA'].mean()
    print("\nRata-rata GPA berdasarkan Gender:")
    print(gpa_by_gender)
except KeyError:
    print("Kolom 'Gender' atau 'GPA' tidak ditemukan dalam dataset.")
except Exception as e:
    print(f"Terjadi kesalahan saat menghitung rata-rata GPA berdasarkan gender: {e}")

# 5. Rata-rata GPA berdasarkan kategori parental support
try:
    gpa_by_Parental_Support = data.groupby('Parental_Support')['GPA'].mean()
    print("\nRata-rata GPA berdasarkan Dukungan Orang Tua:")
    print(gpa_by_Parental_Support)
except KeyError:
    print("Kolom 'Parental_Support' atau 'GPA' tidak ditemukan dalam dataset.")
except Exception as e:
    print(f"Terjadi kesalahan saat menghitung rata-rata GPA berdasarkan dukungan orang tua: {e}")

# 6. Rata-rata GPA berdasarkan kategori parental education
try:
    GPA_by_parental_education = data.groupby('Parental_Education')['GPA'].mean()
    print("\nRata-rata GPA berdasarkan Pendidikan Orang Tua:")
    print(GPA_by_parental_education)
except KeyError:
    print("Kolom 'Parental_Education' atau 'GPA' tidak ditemukan dalam dataset.")
except Exception as e:
    print(f"Terjadi kesalahan saat menghitung rata-rata GPA berdasarkan pendidikan orang tua: {e}")

# 7. Rata-rata GPA berdasarkan kategori ekstrakurikuler
try:
    GPA_by_extracurricular = data.groupby('Extracurricular')['GPA'].mean()
    print("\nRata-rata GPA berdasarkan Kegiatan Ekstrakurikuler:")
    print(GPA_by_extracurricular)
except KeyError:
    print("Kolom 'Extracurricular' atau 'GPA' tidak ditemukan dalam dataset.")
except Exception as e:
    print(f"Terjadi kesalahan saat menghitung rata-rata GPA berdasarkan ekstrakurikuler: {e}")

# 8. Jumlah students yang ikut dan tidak ikut sport
try:
    Sports_distribution = data['Sports'].value_counts()
    print("\nDistribusi Siswa yang Ikut dan Tidak Ikut Olahraga:")
    print(Sports_distribution)
except KeyError:
    print("Kolom 'Sports' tidak ditemukan dalam dataset.")
except Exception as e:
    print(f"Terjadi kesalahan saat menghitung distribusi olahraga: {e}")

# 9. Rata-rata GPA berdasarkan kategori sports
try:
    GPA_by_sports = data.groupby('Sports')['GPA'].mean()
    print("\nRata-rata GPA berdasarkan Olahraga:")
    print(GPA_by_sports)
except KeyError:
    print("Kolom 'Sports' atau 'GPA' tidak ditemukan dalam dataset.")
except Exception as e:
    print(f"Terjadi kesalahan saat menghitung rata-rata GPA berdasarkan olahraga: {e}")

# 10. Jumlah students berdasarkan kategori Music
try:
    Music_distribution = data['Music'].value_counts()
    print("\nDistribusi Siswa berdasarkan Musik:")
    print(Music_distribution)
except KeyError:
    print("Kolom 'Music' tidak ditemukan dalam dataset.")
except Exception as e:
    print(f"Terjadi kesalahan saat menghitung distribusi musik: {e}")

# Visualisasi Distribusi Umur
plt.figure(figsize=(10, 6))
sns.countplot(x='Age', data=data, palette='viridis')
plt.title('Distribusi Umur Siswa')
plt.xlabel('Umur')
plt.ylabel('Jumlah Siswa')
plt.show()

# Visualisasi Rata-rata GPA berdasarkan Gender
plt.figure(figsize=(10, 6))
gpa_by_gender.plot(kind='bar', color=['blue', 'pink'])
plt.title('Rata-rata GPA berdasarkan Gender')
plt.xlabel('Gender')
plt.ylabel('Rata-rata GPA')
plt.xticks(rotation=0)
plt.show()

# Visualisasi Rata-rata GPA berdasarkan Dukungan Orang Tua
try:
    plt.figure(figsize=(10, 6))

    # Periksa apakah variabel berisi data
    if not gpa_by_Parental_Support.empty:
        # Gunakan plt.bar() untuk menghindari potensi masalah dengan .plot()
        plt.bar(gpa_by_Parental_Support.index, gpa_by_Parental_Support.values, color='orange')
        plt.title('Rata-rata GPA berdasarkan Dukungan Orang Tua')
        plt.xlabel('Dukungan Orang Tua')
        plt.ylabel('Rata-rata GPA')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()  # Menyesuaikan tata letak plot
    else:
        print("Tidak ada data untuk divisualisasikan.")

    plt.show()
except AttributeError:
    print("Variabel gpa_by_Parental_Support tidak terdefinisi dengan benar.")
except Exception as e:
    print(f"Terjadi kesalahan saat memvisualisasikan data: {e}")

# Visualisasi Rata-rata GPA berdasarkan Kegiatan Ekstrakurikuler
plt.figure(figsize=(10, 6))
GPA_by_extracurricular.plot(kind='bar', color='green')
plt.title('Rata-rata GPA berdasarkan Kegiatan Ekstrakurikuler')
plt.xlabel('Kegiatan Ekstrakurikuler')
plt.ylabel('Rata-rata GPA')
plt.xticks(rotation=0)
plt.show()

# Visualisasi Rata-rata GPA berdasarkan Olahraga
plt.figure(figsize=(10, 6))
GPA_by_sports.plot(kind='bar', color='purple')
plt.title('Rata-rata GPA berdasarkan Olahraga')
plt.xlabel('Olahraga')
plt.ylabel('Rata-rata GPA')
plt.xticks(rotation=0)
plt.show()

# Visualisasi Distribusi Siswa berdasarkan Musik
plt.figure(figsize=(10, 6))
sns.countplot(x='Music', data=data, palette='pastel')
plt.title('Distribusi Siswa berdasarkan Musik')
plt.xlabel('Musik')
plt.ylabel('Jumlah Siswa')
plt.show()
