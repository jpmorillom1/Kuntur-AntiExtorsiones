from app.core.threat_detector import start_keyword_analysis, handle_transcription
from app.infrastructure.audio_stream import get_audio_chunk

print("🔒 Iniciando sistema Kuntur-AntiExtorsiones...")
start_keyword_analysis()

try:
    while True:
        audio_np = get_audio_chunk()
        handle_transcription(audio_np)
except KeyboardInterrupt:
    print("Finalizando...")
