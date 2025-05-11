import random

def tebakAngka():
    angka = random.randint(1, 100)
    tebakan = 0
    print("Permainan tebak angka.")
    print("Saya menyimpan sebuah angka bulat antara 1 sampai 100. Coba tebak.")
    
    for i in range(1, 8):
        guess = int(input(f"Masukkan tebakan ke-{i}:> "))
        if guess == angka:
            print("Ya. Anda benar")
            return
        elif guess < angka:
            print("Itu terlalu kecil. Coba lagi.")
        else:
            print("Itu terlalu besar. Coba lagi.")
    print("Gagal. Angka yang benar adalah", angka)

tebakAngka()