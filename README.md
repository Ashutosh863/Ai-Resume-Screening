# 📄 AI Resume Screening System (NLP + ML)

An **end-to-end automated resume screening system** that ranks resumes based on their relevance to a given job description using **Natural Language Processing (NLP)** and **Machine Learning**.  
The system exposes a **REST API using FastAPI** and is **Docker-ready** for deployment.

---

## 🚀 Features

- 📑 Automated resume screening
- 🧠 NLP-based text preprocessing
- 📊 TF-IDF vectorization
- 📐 Cosine similarity scoring
- 🏆 Resume ranking by relevance
- 🌐 REST API using FastAPI
- 🐳 Dockerized for easy deployment
- 📘 Interactive Swagger UI

---

## 🛠 Tech Stack

- **Language:** Python  
- **NLP:** NLTK  
- **Machine Learning:** Scikit-learn  
- **Backend:** FastAPI  
- **API Server:** Uvicorn  
- **Containerization:** Docker  

---

## 📁 Project Structure

```
resume_screening/
│
├── app/
│   ├── __init__.py
│   ├── main.py          # FastAPI application
│   ├── model.py         # ML logic (TF-IDF + similarity)
│   └── preprocess.py    # Text preprocessing
│
├── requirements.txt
├── Dockerfile
└── README.md
```

---

## ⚙️ How It Works

1. Job description and resumes are uploaded via API  
2. Text is cleaned and preprocessed  
3. TF-IDF converts text into vectors  
4. Cosine similarity measures relevance  
5. Resumes are ranked based on scores  

---

## 📐 Similarity Technique

- **TF-IDF (Term Frequency–Inverse Document Frequency)**  
- **Cosine Similarity**

---

## ▶️ Run Locally

### Clone Repository
```bash
git clone 
cd resume_screening
```

### Create Virtual Environment
```bash
python -m venv .venv
```

Activate (Windows):
```powershell
.venv\Scripts\Activate.ps1
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Start Server
```bash
uvicorn app.main:app --reload


## 📤 Sample Output

```json
{
  "ranked_resumes": [
    {
      "resume_name": "resume2.txt",
      "similarity_score": 0.89
    },
    {
      "resume_name": "resume1.txt",
      "similarity_score": 0.46
    },
    {
      "resume_name": "resume3.txt",
      "similarity_score": 0.03
    }
  ]
}
```

---

## 🐳 Docker Deployment

```bash
docker build -t resume-screening .
docker run -p 8000:8000 resume-screening
```

---

## 🚀 Future Enhancements

- BERT-based semantic matching
- PDF resume parsing
- Skill extraction
- Database & authentication
- UI dashboard

---
