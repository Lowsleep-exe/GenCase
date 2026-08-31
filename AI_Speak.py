from piper import PiperVoice as pv
import sounddevice as sd
import numpy as np
import os

def speak(text, path):
    voice = pv.load(path)

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

