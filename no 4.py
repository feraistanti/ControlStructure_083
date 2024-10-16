def bilangan_ganjil(n):
     # Loop untuk setiap bilangan dari 1 hingga n
    for i in range(1, n+1):
        # Memeriksa apakah bilangan i adalah ganjil
        if i % 2 != 0:
            print(i, end=' ')  # Mencetak bilangan ganjil tanpa berpindah baris

# Contoh penggunaan
n = int(input("Masukkan nilai n: "))  # Meminta pengguna untuk memasukkan nilai n
print("Bilangan ganjil hingga n:")  # Mencetak judul untuk bilangan ganjil
bilangan_ganjil(n)    # Memanggil fungsi untuk mencetak bilangan ganjil