#==== Percobaan 1 ======
import  time
import random

##def jumlahkan_cara_1(n):
##    hasilnya  =  0
##    for i in range(1, n+1):
##        hasilnya = hasilnya + i
##    return hasilnya
##
##def jumlahkan_cara_2(n):
##    return (n*(n + 1))/2
##
##a = int(input("Masukkan Angka: "))
##
##for i in range(5):
##    awal = time.time()
##    h  =  jumlahkan_cara_1(a)
##    akhir  =  time.time()
##    print("Jumlah Cara 1  adalah  %d,  memerlukan  %9.8f  detik"  %  (h,  akhir-awal))
##print ("\n")
##for i in range(5):
##    awal = time.time()
##    h  =  jumlahkan_cara_2(a)
##    akhir  =  time.time()
##    print("Jumlah Cara 2  adalah  %d,  memerlukan  %9.8f  detik"  %  (h,  akhir-awal))

def insertionSort(A):
    n=len(A)
    for i in range(1, n):
        nilai = A[i]
        pos = i
    while pos > 0 and nilai < A[pos - 1]:
        A[pos] = A[pos - 1]
        pos = pos - 1
    A[pos] = nilai

a = int(input("Masukkan Angka: "))

for i in range(5):
    L=list(range(3000))
    random.shuffle(L)
    awal  =  time.time()
    U  =  insertionSort(L)
    akhir  =  time.time()
    print("Mengurutkan  %d  bilangan,  memerlukan  %8.7f  detik"  %(len(L),akhir-awal))

start = time.time()
sorted_L = insertionSort(L)
end = time.time()

print ("Waktu eksekusi: %f detik"% (end - start))
    
