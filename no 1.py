nilai = input ("Masukkan nilai Anda: ")  # Meminta pengguna untuk memasukkan nilai
nilai = float(nilai)  # Mengubah input menjadi tipe data float untuk evaluasi
if nilai >= 90:  # Memeriksa dan mengevaluasi kinerja berdasarkan nilai
    print ("Exellent performance")
elif nilai >= 80:
    print ("Very good performance")
elif nilai >= 70:
    print ("Good performance")
elif nilai >= 60:
    print ("Average performance")

# Contoh penggunaan
nilai = int(input("Masukkan nilai siswa: "))
print(evaluasi_kinerja(nilai))