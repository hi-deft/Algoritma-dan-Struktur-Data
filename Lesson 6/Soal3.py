# Fungsi untuk melakukan Insertion Sort
def insertion_sort(arr, ascending=True):
    n = len(arr)  # Mendapatkan jumlah elemen dalam array
    
    for i in range(1, n):  # Iterasi dari elemen kedua hingga akhir
        key = arr[i]  # Simpan elemen yang sedang diproses
        j = i - 1  # Mulai membandingkan dengan elemen sebelumnya
        
        # Perulangan untuk menggeser elemen ke kanan hingga menemukan posisi yang benar
        while j >= 0 and ((arr[j] > key and ascending) or (arr[j] < key and not ascending)):
            arr[j + 1] = arr[j]  # Geser elemen ke kanan
            j -= 1  # Pindah ke elemen sebelumnya
        
        arr[j + 1] = key  # Letakkan elemen pada posisi yang benar

# Input jumlah barang
n = int(input("Masukkan jumlah barang: "))

# Input harga barang
harga_barang = []
for i in range(n):
    harga = float(input(f"Masukkan harga barang ke-{i+1}: "))
    harga_barang.append(harga)

# Urutkan harga dari yang termahal ke termurah
insertion_sort(harga_barang, ascending=False)

# Tampilkan hasil sorting
print("\nDaftar Harga Barang dari Termahal ke Termurah:")
for harga in harga_barang:
    print(f"Rp {harga:,.2f}")  # Format tampilan harga dengan 2 desimal dan tanda koma
