def fibonacci(n):
     # Inisialisasi dua variabel untuk menyimpan angka Fibonacci
    a, b = 0, 1
    # Loop untuk mencetak n angka Fibonacci
    for _ in range(n):
        print(a, end=' ')  # Mencetak nilai a tanpa berpindah baris
        a, b = b, a + b  # Memperbarui nilai a dan b untuk langkah berikutnya

# Contoh penggunaan
n = int(input("Masukkan nilai n: "))
print("Deret Fibonacci:")
fibonacci(n)