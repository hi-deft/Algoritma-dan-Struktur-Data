import re

# Teks sumber
text = """Universitas Muhammadiyah Surakarta merupakan salah satu perguruan tinggi swasta unggulan yang terletak di Jawa Tengah. Universitas ini memiliki visi mencetak lulusan yang mampu memberikan kontribusi nyata di masyarakat. Mahasiswa didorong untuk mengembangkan potensi, meneliti isu-isu strategis, dan mewujudkan perubahan positif di berbagai bidang. Kegiatan belajar dilakukan di kampus utama dan di pusat-pusat studi yang tersebar di berbagai lokasi."""

# 1. Ekstrak kata berawalan 'me'
pattern_me = r'\bme[a-z]+\b'  # Pola: 'me' diikuti 1+ huruf kecil
matches_me = re.findall(pattern_me, text, flags=re.IGNORECASE)

# Filter untuk memastikan benar-benar awalan 'me' (case-sensitive)
result_me = [word for word in matches_me if word.startswith('me')]

print("=== HASIL EKSTRAKSI KATA BERAWALAN 'me' ===")
print("Pola regex:", pattern_me)
print("Hasil:", result_me)
print("Jumlah kata:", len(result_me))