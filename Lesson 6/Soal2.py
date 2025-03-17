# Fungsi untuk mengurutkan daftar menggunakan Insertion Sort
def insertion_sort(arr, ascending=True):
    n = len(arr)  # Menentukan jumlah elemen dalam array
    
    # Melakukan iterasi dari elemen kedua hingga terakhir
    for i in range(1, n):
        key = arr[i]  # Simpan elemen saat ini sebagai "key"
        j = i - 1  # Mulai membandingkan dengan elemen sebelumnya
        
        # Perulangan untuk menggeser elemen ke kanan sampai menemukan posisi yang benar
        while j >= 0 and ((arr[j] > key and ascending) or (arr[j] < key and not ascending)):
            arr[j + 1] = arr[j]  # Geser elemen ke kanan
            j -= 1  # Pindah ke elemen sebelumnya
        
        arr[j + 1] = key  # Tempatkan "key" pada posisi yang tepat

# Data tinggi badan atlet dalam cm
tinggi_atlet = [175, 180, 165, 190, 170, 185, 160]

# Membuat salinan daftar untuk menjaga data asli
ascending_order = tinggi_atlet[:]  
insertion_sort(ascending_order, ascending=True)  # Urutkan dari terpendek ke tertinggi
print("Urutan Tinggi dari Terpendek ke Tertinggi:", ascending_order)

# Membuat salinan daftar lainnya
descending_order = tinggi_atlet[:]  
insertion_sort(descending_order, ascending=False)  # Urutkan dari tertinggi ke terpendek
print("Urutan Tinggi dari Tertinggi ke Terpendek:", descending_order)
