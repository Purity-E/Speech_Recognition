from pydub import AudioSegment

# loading wave file
audio_wav = AudioSegment.from_wav("output.wav")

# loading mp3 file 
audio_mp3 = AudioSegment.from_mp3("p_Audio.mp3")

# increasing volume
audio_wav = audio_wav + 6
# repeat clips
audio_wav = audio_wav * 2
# exporting the audio wave file as mp3
audio_wav.export("mash_up.mp3", format="mp3")

print('Done')

