import pyaudio
import numpy as np

sample_rate = 16000
chunk_duration = 3
chunk_size = int(sample_rate * chunk_duration)

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16,
                channels=1,
                rate=sample_rate,
                input=True,
                frames_per_buffer=chunk_size)

def get_audio_chunk():
    data = stream.read(chunk_size, exception_on_overflow=False)
    return np.frombuffer(data, dtype=np.int16).astype(np.float32) / 32768.0
