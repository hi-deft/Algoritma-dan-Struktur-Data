class Produk:
    def __init__(self, kode, nama, harga):
        """Konstruktor untuk inisialisasi atribut produk."""
        self.kode = kode
        self.nama = nama
        self.harga = harga

    def tampilkan_info(self):
        """Menampilkan informasi produk dalam format rapi."""
        print(f"Kode  : {self.kode}")
        print(f"Nama  : {self.nama}")
        print(f"Harga : Rp{self.harga:,.0f}")
        print("-" * 30)


def selection_sort(daftar_produk):
    """Mengurutkan daftar produk berdasarkan harga dari termurah ke termahal menggunakan Selection Sort."""
    n = len(daftar_produk)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if daftar_produk[j].harga < daftar_produk[min_idx].harga:
                min_idx = j
        daftar_produk[i], daftar_produk[min_idx] = daftar_produk[min_idx], daftar_produk[i]


def linear_search(daftar_produk, kode_cari):
    """Mencari produk berdasarkan kode produk menggunakan Linear Search."""
    for produk in daftar_produk:
        if produk.kode == kode_cari:
            return produk
    return None


# Membuat daftar produk
daftar_produk = [
    Produk("P001", "Laptop Asus", 8_500_000),
    Produk("P002", "Smartphone Samsung", 3_200_000),
    Produk("P003", "Monitor LG", 1_800_000),
    Produk("P004", "Keyboard Mechanical", 750_000),
    Produk("P005", "Mouse Gaming", 500_000)
]

# Mengurutkan daftar produk berdasarkan harga
selection_sort(daftar_produk)

# Menampilkan daftar produk setelah diurutkan
print("Daftar Produk Setelah Diurutkan Berdasarkan Harga:")
for produk in daftar_produk:
    produk.tampilkan_info()

# Mencari produk berdasarkan kode
kode_cari = "P003"
hasil_pencarian = linear_search(daftar_produk, kode_cari)

# Menampilkan hasil pencarian
if hasil_pencarian:
    print(f"\nHasil Pencarian Produk dengan Kode {kode_cari}:")
    hasil_pencarian.tampilkan_info()
else:
    print(f"\nProduk dengan kode {kode_cari} tidak ditemukan.")
