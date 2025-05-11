def gambarlahPersegiEmpat(tinggi, lebar):
    for i in range(tinggi):
        if i == 0 or i == tinggi - 1:
            print('0' * lebar)
        else:
            print('0' + ' ' * (lebar - 2) + '0')
# Contoh pemanggilan:
gambarlahPersegiEmpat(4, 5)