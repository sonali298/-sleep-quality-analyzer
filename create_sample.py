import numpy as np
from scipy.io.wavfile import write

# Sample rate and duration
sample_rate = 22050  # Hertz
duration = 2        # Seconds

# Generate a 440 Hz sine wave (A4 note)
t = np.linspace(0, duration, int(sample_rate * duration), False)
note = np.sin(440 * 2 * np.pi * t)

# Ensure that highest value is in 16-bit range
audio = note * (2**15 - 1) / np.max(np.abs(note))
audio = audio.astype(np.int16)

# Save as WAV file
write('audio_samples/sample.wav', sample_rate, audio)
print("Sample audio file created!")
