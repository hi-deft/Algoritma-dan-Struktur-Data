class Buku:
    def __init__(self, judul, pengarang, harga):
        """Konstruktor untuk inisialisasi atribut buku."""
        self.judul = judul
        self.pengarang = pengarang
        self.harga = harga

    def tampilkan_info(self):
        """Menampilkan informasi buku dalam format yang rapi."""
        print(f"Judul    : {self.judul}")
        print(f"Pengarang: {self.pengarang}")
        print(f"Harga    : Rp{self.harga:,.0f}")
        print("-" * 30)

    def ubah_harga(self, harga_baru):
        """Mengubah harga buku."""
        self.harga = harga_baru
        print(f"Harga buku '{self.judul}' telah diperbarui menjadi Rp{self.harga:,.0f}\n")


# Membuat objek buku
buku1 = Buku("Python untuk Pemula", "Qaid Haidar", 150000)
buku2 = Buku("Mastering AI", "Deft Haidar", 225000)

# Menampilkan informasi buku
buku1.tampilkan_info()
buku2.tampilkan_info()

# Mengubah harga buku pertama
buku1.ubah_harga(175000)

# Menampilkan kembali informasi buku setelah perubahan harga
buku1.tampilkan_info()
