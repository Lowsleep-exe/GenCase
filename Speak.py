from piper import PiperVoice as pv
import sounddevice as sd
import numpy as np
import os

voice_path = r"C:\Users\lojei\Documents\Programming\Case GPT\Voices"
voices = os.listdir(voice_path)
voice_files = [ entry for entry in voices if entry.endswith(".onnx") ]

i = 0
for v in voice_files:
    i = i + 1
    print(str(i) + " " + voice_files[i - 1])

choice = int(input("Choose according to the number : "))


path = os.path.join(voice_path, voice_files[choice - 1])
voice = pv.load(path)


text = "Hello. How are you."

audio_chunks = []

for i, chunk in enumerate(voice.synthesize(text)):
    if i > 0:
        pause_seconds = 0.5

        silence = np.zeros(
            int(chunk.sample_rate * pause_seconds),
            dtype=np.float32
        )

        audio_chunks.append(silence)

    audio_chunks.append(chunk.audio_float_array)

audio = np.concatenate(audio_chunks)

sd.play(audio, samplerate=voice.config.sample_rate)
sd.wait()

