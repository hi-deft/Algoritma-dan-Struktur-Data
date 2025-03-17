# Lesson 7 - Quiz Persiapan UTS  

## Soal 1: Sistem Pencatatan Buku di Toko Buku

### Deskripsi Soal
Sebuah toko buku memiliki sistem pencatatan data buku. Setiap buku memiliki informasi **judul, pengarang, dan harga**.
Buatlah program dalam Python dengan konsep **class dan object** untuk:
1. Membuat class `Buku` yang menyimpan informasi buku.
2. Menampilkan informasi buku dalam format yang rapi.
3. Menambahkan metode untuk mengubah harga buku.
4. Membuat minimal 2 objek buku dengan data yang berbeda dan menampilkan informasinya.

### Solusi
- **Class `Buku`** digunakan untuk menyimpan atribut `judul`, `pengarang`, dan `harga`.
- Metode `tampilkan_info()` digunakan untuk menampilkan informasi buku secara rapi.
- Metode `ubah_harga(harga_baru)` memungkinkan perubahan harga buku.
- Program membuat **dua objek buku** dan menampilkan informasinya.
- Salah satu harga buku diperbarui, lalu informasinya ditampilkan kembali.

### Contoh Output
```
Judul    : Python untuk Pemula
Pengarang: Qaid Haidar
Harga    : Rp150,000
------------------------------
Judul    : Mastering AI
Pengarang: Deft Haidar
Harga    : Rp225,000
------------------------------
Harga buku 'Python untuk Pemula' telah diperbarui menjadi Rp175,000

Judul    : Python untuk Pemula
Pengarang: Qaid  Haidar
Harga    : Rp175,000
------------------------------
```

---

## Soal 2: Sistem Pencatatan Produk di Toko Elektronik

### Deskripsi Soal
Sebuah toko elektronik memiliki sistem pencatatan data produk. Setiap produk memiliki **kode produk, nama produk, dan harga**.
Buatlah program dalam Python dengan ketentuan berikut:
1. Buat class `Produk` yang menyimpan data produk.
2. Buat daftar produk yang berisi minimal 5 data produk.
3. Urutkan daftar produk berdasarkan harga dari yang termurah ke yang termahal menggunakan **Selection Sort**.
4. Cari produk berdasarkan kode produk menggunakan **Linear Search**.
5. Tampilkan hasil daftar produk yang telah diurutkan dan hasil pencarian produk berdasarkan kode produk.

### Solusi
- **Class `Produk`** digunakan untuk menyimpan atribut `kode`, `nama`, dan `harga`.
- Metode **Selection Sort** digunakan untuk mengurutkan produk berdasarkan harga.
- Metode **Linear Search** digunakan untuk mencari produk berdasarkan kode.
- Program membuat daftar **5 produk** dan mengurutkannya berdasarkan harga.
- Program kemudian mencari produk berdasarkan kode tertentu dan menampilkan hasilnya.

### Contoh Output
```
Daftar Produk Setelah Diurutkan Berdasarkan Harga:
Kode  : P005
Nama  : Mouse Gaming
Harga : Rp500,000
------------------------------
Kode  : P004
Nama  : Keyboard Mechanical
Harga : Rp750,000
------------------------------
Kode  : P003
Nama  : Monitor LG
Harga : Rp1,800,000
------------------------------
Kode  : P002
Nama  : Smartphone Samsung
Harga : Rp3,200,000
------------------------------
Kode  : P001
Nama  : Laptop Asus
Harga : Rp8,500,000
------------------------------

Hasil Pencarian Produk dengan Kode P003:
Kode  : P003
Nama  : Monitor LG
Harga : Rp1,800,000
------------------------------
```

---

### Kesimpulan
Program ini menunjukkan cara menggunakan **class dan object** dalam Python untuk mengelola data buku dan produk. Program juga menerapkan **algoritma pengurutan dan pencarian** untuk mengelola daftar produk secara efisien.