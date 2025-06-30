from faster_whisper import WhisperModel

# Carga del modelo Whisper
whisper_model = WhisperModel("base", device="cpu", compute_type="int8")
