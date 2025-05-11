def jumlahhurufKonsonan(s):
    total, vokal = jumlahhurufVokal(s)
    return (total, total - vokal)
# Contoh pemanggilan:
print(jumlahhurufKonsonan('Surakarta'))  # (9, 5)