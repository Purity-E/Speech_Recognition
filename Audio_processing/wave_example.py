# importing modules
import wave
import matplotlib.pyplot as plt 
import numpy as np
# reading/loading wave file
obj = wave.open('audio_file.wav', 'rb')
#printing number of channels, sample width, frames and parameters
print('Number of channnels:', obj.getnchannels())
print('Sample width:', obj.getsampwidth())
print('Number of frames:', obj.getnframes())
print('Parameters:', obj.getparams())
# calculating audio time
time = obj.getnframes() / obj.getframerate()
print(time)

#plotting audio file 
# getting the parameters needed for plotting
sample_freq = obj.getframerate()
n_samples = obj.getnframes()
signal_wave = obj.readframes(-1)

obj.close()

# creating a numpy object from signal wave
signal_array = np.frombuffer(signal_wave, dtype=np.int16)

# object from the x-axis which is time
times = np.linspace(0, time, num=n_samples)

plt.figure(figsize=(15, 5))
plt.plot(times, signal_array)
plt.title('Audio Plot')
plt.ylabel(' signal wave')
plt.xlabel('time (s)')
plt.xlim(0, time) #limiting the x axis to the audio time
plt.show()

