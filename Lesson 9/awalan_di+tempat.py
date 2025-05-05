import re

# Teks sumber
text = """Universitas Muhammadiyah Surakarta merupakan salah satu perguruan tinggi swasta unggulan yang terletak di Jawa Tengah. Universitas ini memiliki visi mencetak lulusan yang mampu memberikan kontribusi nyata di masyarakat. Mahasiswa didorong untuk mengembangkan potensi, meneliti isu-isu strategis, dan mewujudkan perubahan positif di berbagai bidang. Kegiatan belajar dilakukan di kampus utama dan di pusat-pusat studi yang tersebar di berbagai lokasi."""

# 3. Ekstrak kata depan 'di' beserta tempat
pattern_di_tempat = r'\b(di)\s+([a-zA-Z]+)\b'  # Pola: 'di' diikuti spasi dan 1+ huruf
matches_di_tempat = re.findall(pattern_di_tempat, text, flags=re.IGNORECASE)

# Gabungkan 'di' dengan kata berikutnya
result_di_tempat = [f"{di} {tempat}" for di, tempat in matches_di_tempat]

print("\n=== HASIL EKSTRAKSI KATA DEPAN 'di' + TEMPAT ===")
print("Pola regex:", pattern_di_tempat)
print("Hasil:", result_di_tempat)
print("Jumlah pasangan:", len(result_di_tempat))