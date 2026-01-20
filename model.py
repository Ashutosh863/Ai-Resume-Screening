from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from app.preprocess import clean_text

class ResumeScreeningModel:

    def __init__(self):
        self.vectorizer = TfidfVectorizer()

    def rank_resumes(self, job_desc: str, resumes: list):
        job_desc = clean_text(job_desc)
        resumes = [clean_text(resume) for resume in resumes]

        corpus = [job_desc] + resumes
        tfidf_matrix = self.vectorizer.fit_transform(corpus)

        similarity_scores = cosine_similarity(
            tfidf_matrix[0:1],
            tfidf_matrix[1:]
        ).flatten()

        ranked = sorted(
            zip(resumes, similarity_scores),
            key=lambda x: x[1],
            reverse=True
        )

        return ranked
