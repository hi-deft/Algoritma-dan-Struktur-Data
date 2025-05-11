from math import sqrt as akar

def selesaikanABC(a, b, c):
    a = float(a)
    b = float(b)
    c = float(c)
    D = b**2 - 4*a*c  # Perbaikan: operator pangkat adalah **, bukan *2
    x1 = (-b + akar(D)) / (2*a)
    x2 = (-b - akar(D)) / (2*a)
    hasil = (x1, x2)
    return hasil

# Contoh penggunaan fungsi
k = selesaikanABC(1, -5, 6)
print(k)  # Output: (3.0, 2.0)