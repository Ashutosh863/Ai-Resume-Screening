from fastapi import FastAPI, UploadFile, File
from app.model import ResumeScreeningModel

app = FastAPI()
model = ResumeScreeningModel()

@app.post("/rank-resumes/")
async def rank_resumes(
    job_description: UploadFile = File(...),
    resumes: list[UploadFile] = File(...)
):
    job_text = (await job_description.read()).decode("utf-8")

    resume_texts = []
    resume_names = []

    for resume in resumes:
        text = (await resume.read()).decode("utf-8")
        resume_texts.append(text)
        resume_names.append(resume.filename)

    results = model.rank_resumes(job_text, resume_texts)

    response = []
    for i, (resume, score) in enumerate(results):
        response.append({
            "resume_name": resume_names[i],
            "similarity_score": round(float(score), 3)
        })

    return {
        "ranked_resumes": sorted(
            response,
            key=lambda x: x["similarity_score"],
            reverse=True
        )}
