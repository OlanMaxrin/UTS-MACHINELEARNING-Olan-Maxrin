import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Mendefinisikan data
data = {
    "fakultas": ["Bisnis", "D3 Perhotelan", "ICT", "Ilmu Komunikasi", "Seni dan Desain"],
    "jumlah_mahasiswa": [260, 28, 284, 465, 735],
    "akreditasi": ["A", "A", "B", "A", "A"]
}

# Membuat DataFrame
info_mahasiswa = pd.DataFrame(data)
print(info_mahasiswa)  # Opsional: Untuk memeriksa DataFrame

# Membuat plot
plt.figure(figsize=(10,2))
sns.barplot(data=info_mahasiswa, x="fakultas", y="jumlah_mahasiswa", palette="viridis")

# Menambahkan judul dan label
plt.title("Jumlah Mahasiswa per Fakultas")
plt.xlabel("Fakultas")
plt.ylabel("Jumlah Mahasiswa")

# Menampilkan plot
plt.show()