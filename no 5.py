def pola_angka(n):
    for i in range(1, n + 1):  # Loop untuk setiap baris
        for j in range(i):     # Loop untuk mencetak angka di setiap baris
            print(i, end=' ')
        print()  # Pindah ke baris berikutnya

# Contoh penggunaan
n = int(input("Masukkan nilai n: "))    # Meminta pengguna untuk memasukkan nilai n
print("Pola angka:")   # Mencetak judul untuk pola angka
pola_angka(n)    # Memanggil fungsi pola_angka untuk mencetak pola