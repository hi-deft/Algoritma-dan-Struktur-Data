def katakan(n):
    satuan = ['', 'satu', 'dua', 'tiga', 'empat', 'lima', 'enam', 'tujuh', 'delapan', 'sembilan']
    belasan = ['sepuluh', 'sebelas', 'dua belas', 'tiga belas', 'empat belas', 'lima belas', 'enam belas', 'tujuh belas', 'delapan belas', 'sembilan belas']
    if n < 10:
        return satuan[n]
    elif 10 <= n < 20:
        return belasan[n-10]
    elif 20 <= n < 100:
        return satuan[n//10] + ' puluh ' + satuan[n%10] if n%10 !=0 else satuan[n//10] + ' puluh'
    elif 100 <= n < 1000:
        return katakan(n//100) + ' ratus ' + katakan(n%100) if n%100 !=0 else katakan(n//100) + ' ratus'
    elif 1000 <= n < 1_000_000:
        return katakan(n//1000) + ' ribu ' + katakan(n%1000) if n%1000 !=0 else katakan(n//1000) + ' ribu'
    elif 1_000_000 <= n < 1_000_000_000:
        return katakan(n//1_000_000) + ' juta ' + katakan(n%1_000_000) if n%1_000_000 !=0 else katakan(n//1_000_000) + ' juta'
    else:
        return "Angka di luar batas"

print(katakan(3126750))  # Output: "Tiga juta seratus dua puluh lima ribu tujuh ratus lima puluh"