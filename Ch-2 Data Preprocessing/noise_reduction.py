import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter1d

np.random.seed(42)
t = np.linspace(0,10,100)
signal = np.sin(2 * np.pi * 5 * t) + 0.2 * np.random.randn(100)
signal[30]+=2.0
signal[70] -=1.5
plt.figure(figsize=(10,4))
plt.subplot(1,2,1)
plt.plot(t, signal, label = 'Original Signal with Noise')
plt.title('Original Signal with Noise')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.legend()

# Gaussian filter for noise reduction 
smoothed_signal = gaussian_filter1d(signal, sigma=1)
plt.subplot(1,2,2)
plt.plot(t, smoothed_signal, label = 'Smoothed Signal')
plt.title('Smoothed Signal (Noise Reduction)')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.legend()
plt.tight_layout()
plt.show()