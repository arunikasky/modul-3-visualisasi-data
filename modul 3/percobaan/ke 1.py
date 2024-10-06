import numpy as np
import matplotlib.pyplot as plt

# Diberikan
h0 = 100  # Ketinggian awal dalam meter
g = 9.8   # Percepatan gravitasi dalam m/s^2

# 1. Hitung waktu jatuh menggunakan persamaan: t = sqrt(2 * h0 / g)
t_fall = np.sqrt(2 * h0 / g)
print(f"Waktu untuk mencapai tanah: {t_fall:.2f} detik")

# 2. Grafik kecepatan sebagai fungsi waktu: v(t) = g * t
time = np.linspace(0, t_fall, 500)
velocity = g * time

# 3. Grafik posisi (ketinggian) sebagai fungsi waktu: h(t) = h0 - 0.5 * g * t^2
position = h0 - 0.5 * g * time**2

# Plot grafik kecepatan vs waktu
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.plot(time, velocity, label='v(t) = g * t', color='blue')
plt.title('Grafik Kecepatan sebagai Fungsi Waktu')
plt.xlabel('Waktu (detik)')
plt.ylabel('Kecepatan (m/s)')
plt.grid(True)
plt.legend()

# Plot grafik posisi vs waktu
plt.subplot(1, 2, 2)
plt.plot(time, position, label='h(t) = h0 - 0.5 * g * t^2', color='green')
plt.title('Grafik Posisi sebagai Fungsi Waktu')
plt.xlabel('Waktu (detik)')
plt.ylabel('Posisi (meter)')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
