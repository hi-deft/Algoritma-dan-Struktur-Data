def formatRupiah(n):
    reversed_str = str(n)[::-1]
    ribuan = '.'.join(reversed_str[i:i+3] for i in range(0, len(reversed_str), 3))
    formatted = ribuan[::-1].replace('..', '.')
    return f'Rp {formatted}'
# Contoh pemanggilan:
print(formatRupiah(2560000))  # Rp 2.560.000