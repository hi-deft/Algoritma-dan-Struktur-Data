# Fungsi untuk melakukan pengurutan menggunakan Insertion Sort
def insertion_sort(arr, ascending=True):
    n = len(arr)  # Mendapatkan jumlah elemen dalam array
    
    # Iterasi dimulai dari elemen kedua hingga akhir
    for i in range(1, n):
        key = arr[i]  # Menyimpan elemen yang sedang diproses
        j = i - 1  # Mulai membandingkan dengan elemen sebelumnya
        
        # Perulangan untuk menggeser elemen ke kanan hingga menemukan posisi yang benar
        while j >= 0 and ((arr[j] > key and ascending) or (arr[j] < key and not ascending)):
            arr[j + 1] = arr[j]  # Geser elemen ke kanan
            j -= 1  # Pindah ke elemen sebelumnya
        
        arr[j + 1] = key  # Letakkan elemen pada posisi yang benar

# Contoh daftar nilai mahasiswa
nilai_mahasiswa = [78, 95, 62, 88, 75, 90, 80]

# Urutkan dari terendah ke tertinggi
ascending_order = nilai_mahasiswa[:]  # Salin daftar agar data asli tidak berubah
insertion_sort(ascending_order, ascending=True)  # Panggil fungsi dengan ascending=True
print("Urutan Nilai dari Terendah ke Tertinggi:", ascending_order)

# Urutkan dari tertinggi ke terendah
descending_order = nilai_mahasiswa[:]  # Salin daftar agar data asli tidak berubah
insertion_sort(descending_order, ascending=False)  # Panggil fungsi dengan ascending=False
print("Urutan Nilai dari Tertinggi ke Terendah:", descending_order)
