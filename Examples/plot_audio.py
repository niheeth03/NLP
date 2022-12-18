import wave
import numpy as np
import matplotlib.pyplot as plt


obj=wave.open("gettysburg.wav","rb")

sample_freq=obj.getframerate()
n_samples=obj.getnframes()
signal_wave=obj.readframes(-1)

obj.close()

t_audio=n_samples/sample_freq
print(t_audio)
times=np.linspace(0,t_audio,num=n_samples)

signal_array=np.frombuffer(signal_wave,dtype=np.int16)
plt.figure(figsize=(15,5))
plt.plot(times,signal_array)
plt.title("Audio signal")
plt.show()
