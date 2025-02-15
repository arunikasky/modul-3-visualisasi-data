import numpy as np
import matplotlib.pyplot as plt

v0 = 0
g = 9.8

# definisi kecepatan sebagai fungsi waktu
def kecepatan(t):
    return g * t

# definisi ketinggian sebagai fungsi waktu
def posisi(t, h0):
    return h0 - 0.5 * g * t**2

# Function to calculate fall time
def fall_time(h0):
    return np.sqrt((2 * h0) / g)

# Set initial height h0 (you can change this value)
h0 = 250  # initial height in meters

# Calculate time to hit the ground
t_fall = fall_time(h0)

# Output fall time
print(f"Waktu yang diperlukan untuk benda mencapai tanah: {t_fall:.2f} detik")

# Create time array for plotting (from 0 to t_ground)
t = np.linspace(0, t_fall, 500)

# Calculate velocity and position over time
v = kecepatan(t)
h = posisi(t, h0)

# Plot kecepatan benda sebagai fungsi waktu selama benda jatuh
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.plot(t, v, label="Kecepatan (v(t))", color='red')
plt.xlabel('Waktu (s)')
plt.ylabel('Kecepatan (m/s)')
plt.title('Kecepatan benda pada waktu jatuh')
plt.grid(True)

# Plot posisi benda sebagai fungsi waktu selama benda jatuh
plt.subplot(1, 2, 2)
plt.plot(t, h, label="Posisi (h(t))", color='blue')
plt.xlabel('Waktu (s)')
plt.ylabel('Ketinggian (m)')
plt.title('Posisi benda pada waktu jatuh')
plt.grid(True)

plt.tight_layout()
plt.show()
