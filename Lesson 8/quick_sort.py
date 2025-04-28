# Data harga produk
harga_produk = [250000, 150000, 300000, 100000, 200000, 350000, 180000]

# Implementasi Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x <= pivot]
        right = [x for x in arr[1:] if x > pivot]
        return quick_sort(left) + [pivot] + quick_sort(right)

# Panggil fungsi quick_sort
harga_terurut = quick_sort(harga_produk)

# Tampilkan hasil
print("Hasil harga produk setelah diurutkan:")
for harga in harga_terurut:
    print(f"Rp {harga:,}")
