import numpy as np
import matplotlib.pyplot as plt

# Given values
h0 = 100  # Initial height in meters
g = 9.8   # Gravitational acceleration in m/s^2

# Calculate the time to reach the ground
t_fall = np.sqrt(2 * h0 / g)

# Create a time array from 0 to t_fall with small intervals for plotting
time = np.linspace(0, t_fall, 500)

# Velocity as a function of time: v(t) = g * t
velocity = g * time

# Position (height) as a function of time: h(t) = h0 - 0.5 * g * t^2
position = h0 - 0.5 * g * time**2

# Plot velocity vs time
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.plot(time, velocity, label='v(t) = g * t', color='blue')
plt.title('Velocity as a Function of Time')
plt.xlabel('Time (s)')
plt.ylabel('Velocity (m/s)')
plt.grid(True)
plt.legend()

# Plot position vs time
plt.subplot(1, 2, 2)
plt.plot(time, position, label='h(t) = h0 - 0.5 * g * t^2', color='green')
plt.title('Position as a Function of Time')
plt.xlabel('Time (s)')
plt.ylabel('Position (m)')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()

# Output the time it takes for the object to hit the ground
t_fall
