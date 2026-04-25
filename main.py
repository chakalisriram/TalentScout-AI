import os
import json
import asyncio
from typing import List
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
import uvicorn
from dotenv import load_dotenv

os.environ["PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION"] = "python"
load_dotenv()

app = FastAPI(title="TalentScout AI | Hackathon Edition")
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite", temperature=0.1)
json_parser = JsonOutputParser()

class JobDescription(BaseModel):
    text: str

# ==========================================
# --- OPTIMIZED AI CHAINS ---
# ==========================================

# 1. JD Parser
jd_chain = PromptTemplate.from_template(
    "Analyze JD: {jd_text}. Return ONLY JSON: {{'role': 'str', 'keywords': ['skill1', 'skill2']}}"
) | llm | json_parser

# 2. Matchmaker
match_chain = PromptTemplate.from_template(
    "Compare JD: {jd_json} with Candidate: {cand_json}. "
    "Return ONLY JSON: {{'score': int, 'reason': '1 sentence'}}"
) | llm | json_parser

# 3. The ALL-IN-ONE Engagement Agent (Massive Speed Boost!)
engagement_chain = PromptTemplate.from_template(
    "Simulate a recruiter engaging a candidate. \n"
    "Role: {role} \n"
    "Candidate: {name} (Skills: {skills}, Availability: {availability}) \n"
    "Return ONLY JSON with EXACTLY these keys: \n"
    "{{"
    "\"outreach\": \"1 sentence recruiter message\", "
    "\"reply\": \"1 sentence candidate reply based on their availability\", "
    "\"interest_score\": 85, "
    "\"interest_reason\": \"1 sentence explanation of their interest score\""
    "}}"
) | llm | json_parser

# ==========================================
# --- API ENDPOINTS ---
# ==========================================

@app.get("/", response_class=HTMLResponse)
async def serve_ui():
    with open("index.html", "r", encoding="utf-8") as f: return f.read()

@app.post("/scout")
async def scout_talent(jd: JobDescription):
    try:
        # STEP 1: Analyze JD (Using ainvoke for speed)
        try:
            jd_analysis = await jd_chain.ainvoke({"jd_text": jd.text})
            keywords = [k.lower() for k in jd_analysis.get('keywords', [])]
        except Exception:
            keywords = jd.text.lower().split()[:10]
            jd_analysis = {"role": "Software Professional", "keywords": keywords}

        # STEP 2: Local Pre-Filter
        with open("candidates.json", "r") as f:
            all_candidates = json.load(f)

        def get_local_score(c):
            cand_skills = [s.lower() for s in c.get('skills', [])]
            return len(set(keywords) & set(cand_skills))

        top_candidates = sorted(all_candidates, key=get_local_score, reverse=True)[:3]
        results = []
        
        # STEP 3: Parallel AI Execution
        for c in top_candidates:
            try:
                # Reduced sleep time drastically!
                await asyncio.sleep(0.5) 
                skills_str = ", ".join(c.get('skills', []))
                
                # Create background tasks
                match_task = match_chain.ainvoke({
                    "jd_json": json.dumps(jd_analysis),
                    "cand_json": json.dumps(c)
                })
                
                eng_task = engagement_chain.ainvoke({
                    "name": c['name'], 
                    "role": jd_analysis.get('role', 'Engineer'), 
                    "skills": skills_str,
                    "availability": c.get('availability', 'Unknown')
                })

                # AWAIT BOTH TASKS AT THE SAME TIME (Parallel Processing)
                match_analysis, eng_analysis = await asyncio.gather(match_task, eng_task)

                # Calculate Final Score
                match_score = match_analysis.get("score", 0)
                int_score = eng_analysis.get("interest_score", 0)
                final_score = (match_score * 0.7) + (int_score * 0.3)
                
                results.append({
                    "name": c.get("name"),
                    "final_score": round(final_score, 2),
                    "match_score": match_score,
                    "match_reason": match_analysis.get("reason", "Strong skill overlap."),
                    "interest_score": int_score,
                    "interest_reason": eng_analysis.get("interest_reason", "Interest assessed."),
                    "skills": c.get("skills", []),
                    "outreach": eng_analysis.get("outreach", "Hi, we have a role for you."),
                    "simulated_reply": eng_analysis.get("reply", "Thanks, I am interested.")
                })
                
            except Exception as e:
                # Fallback
                local_match = get_local_score(c)
                mock_match_score = min(95, 60 + (local_match * 10))
                mock_int_score = 75 if c.get('availability') != 'Immediate' else 95
                mock_final = (mock_match_score * 0.7) + (mock_int_score * 0.3)
                
                results.append({
                    "name": c.get("name"),
                    "final_score": round(mock_final, 2),
                    "match_score": mock_match_score,
                    "match_reason": "API Throttled. Score based on keyword density.",
                    "interest_score": mock_int_score,
                    "interest_reason": f"Fallback calculation based on {c.get('availability')} availability.",
                    "skills": c.get("skills", []),
                    "outreach": f"Hi {c.get('name')}, we have a great role for someone with your background.",
                    "simulated_reply": f"Thanks! I am currently looking and my availability is {c.get('availability')}."
                })

        sorted_results = sorted(results, key=lambda x: x['final_score'], reverse=True)
        return {"results": sorted_results}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
    
    