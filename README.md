
# 🚀 AI-Powered Job Description Analyzer API

An intelligent backend system that analyzes job descriptions using **FastAPI + LangChain + Google Gemini AI**.
It can extract skills, generate interview questions, and evaluate candidate-job fit.

---

## 📌 Features

* 🔍 Extract key skills from Job Descriptions
* 🤖 Generate interview questions dynamically
* 📊 Analyze JD and provide structured insights
* ⚡ FastAPI-based high-performance backend
* 🔗 Easily integrable with frontend apps (React, etc.)

---

## 🏗️ Tech Stack

* **Backend:** FastAPI
* **LLM:** Google Gemini (via LangChain)
* **Framework:** LangChain
* **Server:** Uvicorn
* **Language:** Python

---

## 📂 Project Structure

```
.
├── main.py
├── requirements.txt
├── .env
├── README.md
└── venv/
```

---

## ⚙️ System Architecture

```
Client (Postman / Frontend)
            |
            v
        FastAPI Server
            |
            v
      LangChain Layer
            |
            v
   Google Gemini API
            |
            v
       Response Output
```

---

## 🔁 Program Flow

```
1. User sends Job Description (JD)
2. FastAPI receives request
3. Input passed to LangChain
4. Prompt formatted using template
5. Gemini LLM processes request
6. Response returned to FastAPI
7. JSON response sent back to client
```

---

## 📊 UML Diagram (Sequence Diagram)

```
User        FastAPI        LangChain        Gemini API
 |             |               |                 |
 |  Send JD    |               |                 |
 |-----------> |               |                 |
 |             | Process Req   |                 |
 |             |-------------> |                 |
 |             |               | Format Prompt   |
 |             |               |---------------> |
 |             |               |   Generate      |
 |             |               | <-------------- |
 |             | Get Response  |                 |
 |             | <-------------|                 |
 | JSON Output |               |                 |
 | <-----------|               |                 |
```

---

## 🧠 Example Use Cases

* Resume vs JD matching
* Skill extraction
* Interview preparation
* AI-powered HR tools

---

## 🔑 Environment Variables

Create a `.env` file:

```
GOOGLE_API_KEY=your_api_key_here
```

---

## ▶️ How to Run the Project

### 1️⃣ Clone the Repository

```
git clone <your-repo-url>
cd <project-folder>
```

---

### 2️⃣ Create Virtual Environment

```
python -m venv venv
```

Activate:

```
venv\Scripts\activate   (Windows)
```

---

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

### 4️⃣ Run the Server

```
uvicorn main:app --reload
```

---

### 5️⃣ Access API

Open:

```
http://127.0.0.1:8000/docs
```

---

## 📬 Sample API Request

**POST /analyze**

```json
{
  "job_description": "We are looking for a Software Engineer..."
}
```

---

## 📤 Sample Response

```json
{
  "skills": ["Python", "FastAPI", "DSA"],
  "interview_questions": [
    "Explain REST APIs",
    "What is FastAPI?"
  ]
}
```

---

## ⚠️ Notes

* Ensure correct Python version (**3.10+ recommended**)
* Install all dependencies properly
* Keep API keys secure

---

## 🚀 Future Enhancements

* Resume upload & matching
* Scoring system (ATS-like)
* Frontend dashboard
* Deployment (AWS / Render / Vercel)

---

## 👨‍💻 Author

**Navaneeth Indarapu**

* Final Year CSE (2026)
* Passionate about DSA & Web Development

---

## ⭐ Contribute

Pull requests are welcome. For major changes, open an issue first.

---

## 📄 License

This project is open-source and available under the MIT License.

## System Architecture

Our platform utilizes an asynchronous, parallel-processing architecture to ensure rapid candidate evaluation without hitting API bottlenecks.

```mermaid
graph TD
    %% Styling
    classDef frontend fill:#3b82f6,stroke:#1d4ed8,stroke-width:2px,color:#fff;
    classDef backend fill:#10b981,stroke:#047857,stroke-width:2px,color:#fff;
    classDef engine fill:#8b5cf6,stroke:#6d28d9,stroke-width:2px,color:#fff;
    classDef external fill:#f59e0b,stroke:#b45309,stroke-width:2px,color:#fff;

    %% Nodes
    A[Recruiter Dashboard UI]:::frontend
    B(FastAPI Async Server):::backend
    C{Evaluation Engines}:::engine
    D[Semantic Match Engine <br> 70% Weight]:::engine
    E[Agentic Chat Simulator <br> 30% Weight]:::engine
    F[(Google Gemini API)]:::external
    G[Final Ranked Shortlist]:::backend

    %% Flow
    A -->|Submit Job Description| B
    B -->|Asyncio.gather| C
    C -->|Parse JD & Skills| D
    C -->|Simulate Candidate Outreach| E
    D -->|Match Prompt| F
    E -->|Chat Prompt| F
    F -->|Match Reasoning| D
    F -->|Interest & Availability| E
    D --> G
    E --> G
    G -->|JSON Response| A








