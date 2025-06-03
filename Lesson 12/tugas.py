import time
import random

# =======================
# 1. Efisiensi Algoritma Pencarian
# =======================

def linear_search(arr, target):
    """Pencarian Linear: cek satu per satu dari awal hingga akhir."""
    for i in arr:
        if i == target:
            return True
    return False

def binary_search(arr, target):
    """Pencarian Biner: hanya untuk list terurut."""
    left, right = 0, len(arr)-1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False

print("="*40)
print("1. Efisiensi Algoritma Pencarian")
for n in [10_000, 100_000, 1_000_000]:
    data = list(range(n))
    target = random.choice(data)
    print(f"\nUkuran data: {n}")

    start = time.time()
    linear_search(data, target)
    print("Linear Search : %8.6f detik" % (time.time() - start))

    start = time.time()
    binary_search(data, target)
    print("Binary Search: %8.6f detik" % (time.time() - start))

# =======================
# 2. Analisis Efisiensi Algoritma Sorting Sederhana
# =======================

def bubble_sort(arr):
    """Bubble Sort: Bandingkan dan tukar elemen bersebelahan."""
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def selection_sort(arr):
    """Selection Sort: Pilih elemen terkecil dan tukar ke depan."""
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def insertion_sort(arr):
    """Insertion Sort: Sisipkan elemen ke posisi yang tepat."""
    n = len(arr)
    for i in range(1, n):
        nilai = arr[i]
        pos = i
        while pos > 0 and nilai < arr[pos - 1]:
            arr[pos] = arr[pos - 1]
            pos -= 1
        arr[pos] = nilai

print("\n" + "="*40)
print("2. Analisis Efisiensi Algoritma Sorting Sederhana")
for n in [100, 500, 1000]:
    print(f"\nUkuran data: {n}")
    for sort_func, name in [
        (bubble_sort, "Bubble Sort"),
        (selection_sort, "Selection Sort"),
        (insertion_sort, "Insertion Sort")
    ]:
        data = [random.randint(0, 10000) for _ in range(n)]
        start = time.time()
        sort_func(data)
        print(f"{name:18}: {time.time() - start:8.6f} detik")

# =======================
# 3. Analisis Efisiensi Merge Sort & Quick Sort
# =======================

def merge_sort(arr):
    """Merge Sort: Divide and conquer, hasil akhir in-place."""
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        # Gabungkan hasil L dan R ke arr
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def quick_sort(arr):
    """Quick Sort: Rekursif, tidak in-place (mengembalikan list baru)."""
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x < pivot]
        greater = [x for x in arr[1:] if x >= pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

print("\n" + "="*40)
print("3. Analisis Efisiensi Merge Sort & Quick Sort")
for n in [10_000, 50_000, 100_000]:
    print(f"\nUkuran data: {n}")
    data = [random.randint(0, 1000000) for _ in range(n)]
    arr1 = data.copy()
    arr2 = data.copy()

    start = time.time()
    merge_sort(arr1)
    print(f"Merge Sort : {time.time() - start:8.6f} detik")

    start = time.time()
    quick_sort(arr2)
    print(f"Quick Sort : {time.time() - start:8.6f} detik")

# =======================
# Catatan:
# - Untuk quick_sort, hasil pengurutan tidak disimpan ke arr2 karena fungsi mengembalikan list baru.
# - Untuk data besar, Merge Sort biasanya lebih stabil dan konsisten, sedangkan Quick Sort bisa sangat cepat pada data acak tetapi lambat pada data hampir terurut.
# - Gunakan time.time() sebelum dan sesudah pemanggilan fungsi untuk mengukur waktu eksekusi.
# - Pastikan setiap fungsi sorting menerima salinan data (bukan data asli) agar hasil pengukuran adil.