# **Proyek Ekstraksi Kata dengan Regular Expressions**

Proyek ini berisi script Python untuk mengekstrak kata-kata dari teks berdasarkan awalan tertentu menggunakan regular expressions (regex). Fokus ekstraksi meliputi kata berawalan 'me', 'di', serta kata depan 'di' beserta tempat yang ditunjuknya.

## **Fitur**
1. **Ekstraksi kata berawalan 'me'**  
   Contoh: "memberikan", "mengembangkan"
2. **Ekstraksi kata berawalan 'di'**  
   Termasuk kata kerja pasif dan kata depan
3. **Ekstraksi kata depan 'di' + tempat**  
   Contoh: "di kampus", "di masyarakat"

## Struktur File
ekstraksi_kata/
├── ekstraksi_me.py # Script khusus ekstraksi 'me'
├── ekstraksi_di.py # Script khusus ekstraksi 'di'
├── ekstraksi_di_tempat.py # Script khusus ekstraksi 'di' + tempat
├── ekstraksi_gabungan.py # Script all-in-one
└── contoh_teks.txt # Contoh teks input


## Cara Menggunakan

### 1. Persyaratan
- Python 3.x
- Library `re` (sudah termasuk dalam instalasi standar Python)

### 2. Menjalankan Script
#### Opsi 1: Script Per Fungsi
```bash
# Ekstrak kata berawalan 'me'
python ekstraksi_me.py

# Ekstrak kata berawalan 'di' 
python ekstraksi_di.py

# Ekstrak 'di' + tempat
python ekstraksi_di_tempat.py
**Opsi 2: Script Gabungan
bash
python ekstraksi_gabungan.py
**3. Custom Teks Input
Buka file contoh_teks.txt

Ganti dengan teks Anda

Jalankan script dengan:

bash
python ekstraksi_gabungan.py < contoh_teks.txt
Output Contoh
python
=== HASIL EKSTRAKSI ===
Kata berawalan 'me': ['memiliki', 'mencetak', 'memberikan', ...]
Kata berawalan 'di': ['didorong', 'dilakukan', 'di', ...] 
Kata depan 'di' + tempat: ['di kampus', 'di masyarakat', ...]
Pola Regex yang Digunakan
Fungsi	Pola	Penjelasan
Awalan 'me'	\bme[a-z]+\b	'me' + 1+ huruf kecil
Awalan 'di'	\bdi[a-z]*\b	'di' + 0+ huruf kecil
'di' + tempat	\b(di)\s+([a-zA-Z]+)\b	'di' + spasi + 1 kata
Keterbatasan
Tidak membedakan kata kerja pasif dan kata depan 'di'

Mungkin menghasilkan false positive pada teks kompleks

Untuk analisis lebih akurat, disarankan menggunakan NLP (spaCy/NLTK)

Lisensi
Proyek ini dilisensikan di bawah MIT License.


Catatan:  
1. Simpan sebagai `README.md` di folder proyek  
2. Sesuaikan path file jika struktur folder berbeda  
3. Tambahkan bagian `CONTRIBUTING.md` jika proyek bersifat kolaboratif