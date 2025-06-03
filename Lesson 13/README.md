# Tugas Graf - Representasi & Implementasi

## No. 1: Rute Pengiriman Logistik Internasional

### Deskripsi
Diberikan rute dan biaya pengiriman antar kota besar:
- Jakarta → Singapore (2)
- Jakarta → Kuala Lumpur (3)
- Singapore → Bangkok (4)
- Kuala Lumpur → Bangkok (2)
- Bangkok → Manila (5)
- Singapore → Manila (6)

### Permintaan
- Representasi **Adjacency List** berbobot
- Representasi **Adjacency Matrix** berbobot
- Implementasi keduanya dalam Python

---

## No. 2: Ketergantungan Tugas Proyek

### Deskripsi
Ketergantungan antar tugas:
- A → B, C
- B → D
- C → D, E
- E → A

### Permintaan
- Gambar graf terarah
- Representasi **Edge List**
- Implementasi fungsi Python untuk deteksi siklus (DFS)

---

## No. 3: Jaringan Kereta Bawah Tanah

### Deskripsi
Koneksi antar stasiun:
- A → B, C
- B → D
- C → D, E
- D → F
- E → F

### Permintaan
- Representasi **Adjacency List**
- Gambar graf tak berarah
- Implementasi pencarian rute A ke F menggunakan **BFS**

---

## No. 4: Prasyarat Mata Kuliah

### Deskripsi
Struktur prasyarat:
- Algoritma → Struktur Data
- Struktur Data → Graf, Pemrograman Lanjut
- Pemrograman Dasar → Algoritma
- Basis Data → Sistem Informasi
- Sistem Informasi → Proyek Akhir

### Permintaan
- Representasi graf terarah prasyarat
- Implementasi **Adjacency List** di Python

---

## Struktur File

- `no1_logistik.py` : Representasi dan implementasi graf berbobot (Adjacency List & Matrix)
- `no2_proyek.py`   : Edge List & deteksi siklus pada graf terarah
- `no3_kereta.py`   : Adjacency List & BFS untuk pencarian rute
- `no4_prasyarat.py`: Adjacency List prasyarat mata kuliah

---

## Cara Menjalankan

Jalankan masing-masing file Python sesuai nomor soal:
```bash
python no1_logistik.py
python no2_proyek.py
python no3_kereta.py
python no4_prasyarat.py