from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")


def analyze_job_description(jd_text):
    keywords = [kw.strip() for kw in jd_text.split() if len(kw) > 4]
    jd_embedding = model.encode(jd_text, convert_to_tensor=True)
    return {
        "text": jd_text,
        "keywords": list(set(keywords)),
        "embedding": jd_embedding
    }
