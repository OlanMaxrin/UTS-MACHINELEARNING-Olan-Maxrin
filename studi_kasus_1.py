# Data mahasiswa dan biaya
data = [
    {'hari': 'Senin', 'datang': 2, 'biaya_per_orang': 30000, 'mahasiswa': 'Ani'},
    {'hari': 'Selasa', 'datang': 3, 'biaya_per_orang': 35000, 'mahasiswa': 'Budi'},
    {'hari': 'Rabu', 'datang': 4, 'biaya_per_orang': 25000, 'mahasiswa': 'Jono'},
    {'hari': 'Kamis', 'datang': 1, 'biaya_per_orang': 15000, 'mahasiswa': 'Lono'},
    {'hari': 'Jumat', 'datang': 2, 'biaya_per_orang': 20000, 'mahasiswa': 'Joni'},
    {'hari': 'Sabtu', 'datang': 5, 'biaya_per_orang': 30000, 'mahasiswa': 'Ani'},
    {'hari': 'Minggu', 'datang': 2, 'biaya_per_orang': 35000, 'mahasiswa': 'Budi'}
]

# a) Rata-rata mahasiswa datang pada minggu ini
total_datang = sum(d['datang'] for d in data)
rata_rata_datang = total_datang / len(data)
print(f"Rata-rata mahasiswa datang pada minggu ini: {rata_rata_datang}")

# b) Kapan biaya tertinggi terjadi
max_biaya = max(data, key=lambda x: x['datang'] * x['biaya_per_orang'])
print(f"Biaya tertinggi terjadi pada hari {max_biaya['hari']}")

# c) Hari apa biaya lebih dari 110000
hari_biaya_lebih_110000 = [d['hari'] for d in data if d['datang'] * d['biaya_per_orang'] > 110000]
print(f"Hari dengan biaya lebih dari 110000: {hari_biaya_lebih_110000}")

# d) Siapa yang paling banyak datang ke kampus
from collections import Counter
mahasiswa_counter = Counter(d['mahasiswa'] for d in data)
mahasiswa_terbanyak = mahasiswa_counter.most_common(1)[0]
print(f"Mahasiswa yang paling banyak datang ke kampus: {mahasiswa_terbanyak[0]} dengan {mahasiswa_terbanyak[1]} kali")

# e) Siapa yang datang pada hari minggu
mahasiswa_minggu = [d['mahasiswa'] for d in data if d['hari'] == 'Minggu']
print(f"Mahasiswa yang datang pada hari Minggu: {mahasiswa_minggu}")

# f) Biaya tertinggi dan terendah
biaya_total_per_hari = [d['datang'] * d['biaya_per_orang'] for d in data]
biaya_tertinggi = max(biaya_total_per_hari)
biaya_terendah = min(biaya_total_per_hari)
print(f"Biaya tertinggi: {biaya_tertinggi}, Biaya terendah: {biaya_terendah}")

# g) Frekuensi datang tertinggi dan terendah
frekuensi_tertinggi = max(d['datang'] for d in data)
frekuensi_terendah = min(d['datang'] for d in data)
print(f"Frekuensi datang tertinggi: {frekuensi_tertinggi}, Frekuensi datang terendah: {frekuensi_terendah}")