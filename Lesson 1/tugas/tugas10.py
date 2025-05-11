from math import sqrt as akar

def selesaikanABC(a, b, c):
    D = b**2 - 4*a*c
    if D < 0:
        print("Determinannya negatif. Persamaan tidak mempunyai akar real.")
        return None
    else:
        x1 = (-b + akar(D)) / (2*a)
        x2 = (-b - akar(D)) / (2*a)
        return (x1, x2)
# Contoh pemanggilan:
selesaikanABC(1, 2, 3)  # Pesan error