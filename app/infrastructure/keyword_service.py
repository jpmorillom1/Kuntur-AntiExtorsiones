from keybert import KeyBERT

kw_model = KeyBERT(model="paraphrase-multilingual-MiniLM-L12-v2")

def extract_keywords(text):
    try:
        keywords = kw_model.extract_keywords(
            text,
            keyphrase_ngram_range=(1, 2),
            stop_words=None,
            top_n=5,
            diversity=0.5
        )
        return [kw[0] for kw in keywords if kw[1] > 0.2]
    except Exception as e:
        print(f"Error extrayendo keywords: {e}")
        return []
