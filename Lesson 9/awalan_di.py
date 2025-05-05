import re

# Teks sumber
text = """Universitas Muhammadiyah Surakarta merupakan salah satu perguruan tinggi swasta unggulan yang terletak di Jawa Tengah. Universitas ini memiliki visi mencetak lulusan yang mampu memberikan kontribusi nyata di masyarakat. Mahasiswa didorong untuk mengembangkan potensi, meneliti isu-isu strategis, dan mewujudkan perubahan positif di berbagai bidang. Kegiatan belajar dilakukan di kampus utama dan di pusat-pusat studi yang tersebar di berbagai lokasi."""

# 2. Ekstrak kata berawalan 'di'
pattern_di = r'\bdi[a-z]*\b'  # Pola: 'di' diikuti 0+ huruf kecil
matches_di = re.findall(pattern_di, text, flags=re.IGNORECASE)

# Filter untuk memastikan benar-benar awalan 'di' (case-sensitive)
result_di = [word for word in matches_di if word.startswith('di')]

print("\n=== HASIL EKSTRAKSI KATA BERAWALAN 'di' ===")
print("Pola regex:", pattern_di)
print("Hasil:", result_di)
print("Jumlah kata:", len(result_di))