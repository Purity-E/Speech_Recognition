import pyaudio
import wave

# setting parameters
FRAMES_PER_BUFFER = 3200
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000

# creating a pyaudio object
p = pyaudio.PyAudio()

# creating stream object
stream = p.open(
    frames_per_buffer=FRAMES_PER_BUFFER,
    format=FORMAT,
    channels=CHANNELS,
    rate=RATE,
    input=True
    )

print('Start recording')

seconds = 5 #audio duration
frames = [] #list for storing frames
for i in range(0, int(RATE/FRAMES_PER_BUFFER*seconds)):
    data = stream.read(FRAMES_PER_BUFFER)
    frames.append(data)

# shutting down
stream.stop_stream()
stream.close()
p.terminate()

# saving object in wave file
obj = wave.open('output.wav', 'wb')
# setting parameters
obj.setnchannels(CHANNELS)
obj.setsampwidth(p.get_sample_size(FORMAT))
obj.setframerate(RATE)
obj.writeframes(b"".join(frames))
obj.close()
