def bilangan_terbesar(a, b, c):
    if a >= b and a >= c:    # Memeriksa apakah a adalah bilangan terbesar
        return a  # Mengembalikan a jika a adalah yang terbesar
    elif b >= a and b >= c:   # Memeriksa apakah b adalah bilangan terbesar
        return b
    else:
        return c   # Mengembalikan c sebagai bilangan terbesar

# Contoh penggunaan
a = int(input("Masukkan bilangan pertama: "))
b = int(input("Masukkan bilangan kedua: "))
c = int(input("Masukkan bilangan ketiga: "))
print("Bilangan terbesar adalah:", bilangan_terbesar(a, b, c))