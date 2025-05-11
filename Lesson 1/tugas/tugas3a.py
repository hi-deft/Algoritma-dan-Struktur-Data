def jumlahhurufVokal(s):
    vokal = {'a', 'i', 'u', 'e', 'o', 'A', 'I', 'U', 'E', 'O'}
    total = len(s)
    jumlah = sum(1 for char in s if char in vokal)
    return (total, jumlah)
# Contoh pemanggilan:
print(jumlahhurufVokal('Surakarta'))  # (9, 4)