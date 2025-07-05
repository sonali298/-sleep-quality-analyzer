import matplotlib
matplotlib.use('TkAgg')  # Ensure the correct backend is used

import librosa
import librosa.display
import matplotlib.pyplot as plt

# Path to your sample audio
audio_file = 'audio_samples/sample.wav'

# Load the audio file
y, sr = librosa.load(audio_file)

# Plot the waveform
plt.figure(figsize=(14, 5))
librosa.display.waveshow(y, sr=sr)
plt.title('Waveform of sample.wav')
plt.xlabel('Time (seconds)')
plt.ylabel('Amplitude')
plt.show()
