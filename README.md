# AI-Powered Talent Scouting & Engagement Agent

A prototype for the Catalyst AI Hackathon by Deccan AI that takes a Job Description (JD) as input, discovers matching candidates, engages them conversationally (simulated), and outputs a ranked shortlist scored on Match Score and Interest Score.

## Files

- `candidates.json`: 10 diverse mock candidate profiles
- `main.py`: FastAPI backend with LangChain and Gemini 1.5 Flash implementation
- `requirements.txt`: Python dependencies
- `.env.example`: Example environment variables
- `EXPLAINABILITY.md`: Detailed explanation of the explainability implementation

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Create a `.env` file based on `.env.example` and add your Google Gemini API key:
   ```env
   GOOGLE_API_KEY=your_actual_api_key_here
   ```

3. Run the server:
   ```bash
   uvicorn main:app --reload
   ```

4. The API will be available at `http://localhost:8000`

## API Endpoint

### POST /scout
Submit a job description to get a ranked list of candidates.

**Request Body:**
```json
{
  "text": "Job description text here..."
}
```

**Response:**
```json
{
  "results": [
    {
      "id": "c001",
      "name": "Alex Chen",
      "match_score": 85,
      "match_reasoning": "Strong skills match with 4 years of Python/Django experience aligning well with the required backend technologies.",
      "interest_score": 90,
      "interest_reasoning": "Candidate expresses immediate availability and enthusiasm about the opportunity, indicating strong interest.",
      "final_score": 86.5,
      "outreach_message": "Generated outreach message...",
      "simulated_response": "Simulated candidate response..."
    }
    // ... more candidates ranked by final_score
  ]
}
```

## How It Works

1. **JD Parsing**: Uses Gemini 1.5 Flash to extract structured requirements from the job description.
2. **Candidate Discovery**: Compares parsed JD against the candidate database.
3. **Match Scoring**: Calculates a 0-100 score with one-sentence reasoning using LLM.
4. **Conversational Outreach**: Generates a personalized message and simulates a candidate response.
5. **Interest Scoring**: Analyzes the simulated response for interest level with reasoning.
6. **Final Ranking**: Combines scores with weights (Match × 0.7 + Interest × 0.3).

## Explainability

See `EXPLAINABILITY.md` for details on how the agent provides transparent reasoning for both match and interest scores, allowing recruiters to understand why candidates were ranked highly.

## Notes

- The candidate response simulation is simplified for the prototype. In a production system, this could be replaced with actual outreach or a more sophisticated response generation model.
- The explainability is implemented through prompt engineering, instructing the LLM to provide both a score and a concise reasoning.