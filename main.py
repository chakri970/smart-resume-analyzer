from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from utils.resume_parser import parse_resume
from utils.jd_analyzer import analyze_job_description
from utils.scorer import score_resume_vs_jd
from utils.rewriter import rewrite_resume

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/analyze")
async def analyze_resume(
    resume: UploadFile = File(...),
    job_description: str = Form(...),
    enhance: bool = Form(False)
):
    resume_text = await parse_resume(resume)
    jd_data = analyze_job_description(job_description)
    score, insights = score_resume_vs_jd(resume_text, jd_data)

    rewritten_resume = ""
    if enhance:
        rewritten_resume = rewrite_resume(resume_text, jd_data)

    return {
        "score": score,
        "insights": insights,
        "rewritten_resume": rewritten_resume
    }
