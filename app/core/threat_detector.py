import threading
from collections import deque
from app.infrastructure.whisper_service import whisper_model
from app.infrastructure.keyword_service import extract_keywords

text_buffer = deque(maxlen=5)
keywords_lock = threading.Lock()
current_keywords = []

from app.infrastructure.keyword_service import extract_keywords as extract_kw

def extract_keywords(text):
    return extract_kw(text)


def start_keyword_analysis():
    def keyword_analysis_thread():
        global current_keywords
        while True:
            if text_buffer:
                with keywords_lock:
                    context = " ".join(text_buffer)
                    current_keywords = extract_keywords(context)
            threading.Event().wait(2)

    thread = threading.Thread(target=keyword_analysis_thread, daemon=True)
    thread.start()

def handle_transcription(audio_np):
    segments, _ = whisper_model.transcribe(
        audio_np,
        language="es",
        beam_size=3,
        vad_filter=True,
        without_timestamps=True
    )
    current_text = " ".join(segment.text for segment in segments)
    if current_text.strip():
        text_buffer.append(current_text)
        with keywords_lock:
            if current_keywords:
                print(f"🔑 Palabras clave detectadas: {', '.join(current_keywords)}")
        print(f"Transcripción: {current_text}")
