import numpy as np
import matplotlib.pyplot as plt

# Parameter jatuh bebas
g = 9.8  # Percepatan gravitasi (m/s^2)
h0 = 100  # Ketinggian awal benda (m)

# Menghitung waktu yang diperlukan benda untuk mencapai tanah
T = np.sqrt(2 * h0 / g)

# Waktu untuk perhitungan grafik
t = np.linspace(0, T, 100)

# Persamaan gerak jatuh bebas (kecepatan dan posisi sebagai fungsi waktu)
v = g * t  # Kecepatan sebagai fungsi waktu
h = h0 - 0.5 * g * t**2  # Posisi (ketinggian) sebagai fungsi waktu

# Mencetak hasil perhitungan
print(f"Waktu yang diperlukan benda untuk mencapai tanah: {T} s")
print(f"Kecepatan saat mencapai tanah: {max(v)} m/s")

# Plot grafik kecepatan sebagai fungsi waktu
plt.plot(t, v)
plt.xlabel('Waktu (t) [s]')
plt.ylabel('Kecepatan (v) [m/s]')
plt.title('Grafik Kecepatan sebagai Fungsi Waktu')
plt.grid(True)
plt.show()

# Plot grafik posisi (ketinggian) sebagai fungsi waktu
plt.plot(t, h)
plt.xlabel('Waktu (t) [s]')
plt.ylabel('Ketinggian (h) [m]')
plt.title('Grafik Posisi (Ketinggian) sebagai Fungsi Waktu')
plt.grid(True)
plt.show()
