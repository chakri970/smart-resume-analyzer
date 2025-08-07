from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")


def score_resume_vs_jd(resume_text, jd_data):
    resume_embedding = model.encode(resume_text, convert_to_tensor=True)
    score = util.cos_sim(resume_embedding, jd_data["embedding"]).item()
    score_percentage = round(score * 100, 2)

    missing_keywords = [
        kw for kw in jd_data["keywords"]
        if kw.lower() not in resume_text.lower()
    ]
    insights = {
        "missing_keywords": missing_keywords,
        "total_keywords": len(jd_data["keywords"]),
        "score_percent": score_percentage
    }
    return score_percentage, insights
