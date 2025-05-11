def faktorPrima(n):
    faktor = []
    pembagi = 2
    while pembagi <= n:
        if n % pembagi == 0:
            faktor.append(pembagi)
            n = n // pembagi
        else:
            pembagi += 1
    return tuple(faktor)
# Contoh pemanggilan:
print(faktorPrima(120))  # (2, 2, 2, 3, 5)