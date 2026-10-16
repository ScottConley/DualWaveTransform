import numpy as np
import matplotlib.pyplot as plt

# Set up the time domain system params

sample_rate = 8000
duration = 1.0
t = np.linspace(0, duration, int(sample_rate * duration))

# Construct the composite signal (mixing frequencies)
# Standard A note (440Hz) mixed with its octave (880Hz)

clean_signal = np.sin(2 * np.pi * 440 * t) + np.sin(2 * np.pi * 880 * t)

noise = np.random.normal(0, 2.5, len(clean_signal))

corrupted_signal = clean_signal + noise

# Compute the systems Fast Fourier Transform (Move from time to frequency domain)

fft_output_clean = np.fft.fft(clean_signal)
freq_clean = np.fft.fftfreq(len(clean_signal), 1/sample_rate)

# Filter for positive frequencies

positive_mask_clean = freq_clean > 0

fft_output_corrupt = np.fft.fft(corrupted_signal)
freq_corrupt = np.fft.fftfreq(len(corrupted_signal), 1/sample_rate)

positive_mask_corrupt = freq_corrupt > 0

# Plot the information

plt.figure(figsize=(10, 10))

plt.subplot(4, 1, 1)
plt.plot(t[:150], clean_signal[:150], color = 'blue', linewidth = 2)
plt.title('Stage 1: Clean Time Domain')
plt.xlabel('Time (Seconds)')
plt.ylabel('Amplitude (Voltage/Height)')
plt.grid(True)

plt.subplot(4, 1, 2)

plt.plot(freq_clean[positive_mask_clean], np.abs(fft_output_clean[positive_mask_clean]), color = 'red', linewidth = 2)
plt.xlim(0, 1200)
plt.title("Stage 2: Frequency Domain (Clean)")
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.grid(True)

plt.subplot(4, 1, 3)
plt.plot(t[:150], corrupted_signal[:150], color = 'blue', linewidth = 2)
plt.title('Stage 3: Corrupted Time Domain')
plt.xlabel('Time (Seconds)')
plt.ylabel('Amplitude (Voltage/Height)')
plt.grid(True)

plt.subplot(4, 1, 4)

plt.plot(freq_corrupt[positive_mask_corrupt], np.abs(fft_output_corrupt[positive_mask_corrupt]), color = 'red', linewidth = 2)
plt.xlim(0, 1200)
plt.title("Stage 2: Frequency Domain (Corrupted)")
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.grid(True)

plt.tight_layout()
plt.show()