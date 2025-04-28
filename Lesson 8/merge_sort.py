# Data nilai dari Kelas A dan Kelas B
kelas_A = [75, 60, 82, 55, 90]
kelas_B = [68, 77, 58, 80, 85]

# Gabungkan data
nilai_siswa = kelas_A + kelas_B

# Implementasi Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        # Rekursif sorting
        merge_sort(left)
        merge_sort(right)

        # Penggabungan (merge) array kiri dan kanan
        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        # Cek sisa elemen
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

# Panggil fungsi merge_sort
merge_sort(nilai_siswa)

# Tampilkan hasil
print("Hasil nilai siswa setelah diurutkan:", nilai_siswa)
