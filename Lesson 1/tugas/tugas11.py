def apakahKabisat(tahun):
    return (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0)
# Contoh pemanggilan:
print(apakahKabisat(2000))  # True