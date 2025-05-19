# **Implementasi Stack dan Queue dalam Python**

## **Deskripsi Proyek**
Proyek ini berisi implementasi struktur data **Stack (tumpukan)** dan **Queue (antrian)** menggunakan Python. Studi kasus yang digunakan mencakup:
1. **Manajemen Gudang Kardus** (Stack)
2. **Antrian Bus Sekolah** (Queue)
3. **Sistem Logistik Gudang-ke-Toko** (Stack + Queue)

## **Struktur File**
```
📂 stack-queue-implementation/
├── 📄 gudang_kardus.py       # Implementasi Stack untuk gudang kardus
├── 📄 antrian_bus.py         # Implementasi Queue untuk antrian bus sekolah
├── 📄 logistik_gudang.py     # Implementasi Stack & Queue untuk sistem logistik
└── 📄 laporan.pdf            # Laporan lengkap analisis studi kasus
```

## **Cara Menjalankan Program**
1. **Clone repositori**:
   ```bash
   git clone [URL_REPOSITORY]
   cd stack-queue-implementation
   ```

2. **Jalankan file Python**:
   - Untuk simulasi gudang kardus:
     ```bash
     python gudang_kardus.py
     ```
   - Untuk simulasi antrian bus:
     ```bash
     python antrian_bus.py
     ```
   - Untuk simulasi logistik gudang:
     ```bash
     python logistik_gudang.py
     ```

## **Fitur Implementasi**
### **1. Stack (Gudang Kardus)**
- **Method**:
  - `push()`: Menambahkan kardus ke tumpukan.
  - `pop()`: Mengeluarkan kardus teratas.
  - `is_empty()`: Memeriksa apakah tumpukan kosong.
- **Keluaran**:
  ```
  Kardus tersisa di gudang: ['A', 'B']
  ```

### **2. Queue (Antrian Bus)**
- **Method**:
  - `enqueue()`: Menambahkan siswa ke antrian.
  - `dequeue()`: Mengeluarkan siswa paling depan.
  - `is_empty()`: Memeriksa apakah antrian kosong.
- **Keluaran**:
  ```
  Siswa yang naik bus pertama: ['Andi', 'Budi', 'Cici', 'Dedi', 'Eni']
  Siswa yang menunggu: ['Farah', 'Gani']
  ```

### **3. Hybrid Stack + Queue (Sistem Logistik)**
- **Stack** untuk menyimpan barang di gudang.
- **Queue** untuk mengatur pengiriman barang ke toko.
- **Keluaran**:
  ```
  Isi tumpukan di gudang: ['Sabun']
  Urutan pengiriman ke toko: Shampoo → Sikat Gigi
  Barang terakhir sampai di toko: Sikat Gigi
  ```

## **Kebutuhan Sistem**
- Python 3.x
- Tidak memerlukan library eksternal.

## **Pembelajaran**
- **Stack** menggunakan prinsip **LIFO (Last-In-First-Out)**.
- **Queue** menggunakan prinsip **FIFO (First-In-First-Out)**.
- Kombinasi Stack dan Queue dapat memodelkan alur kerja kompleks (contoh: logistik).

---

**✨ Tip**: Gunakan visualisasi diagram untuk memahami alur data!  