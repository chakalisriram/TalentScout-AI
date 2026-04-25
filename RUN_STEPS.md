# Steps to Run the AI-Powered Talent Scouting Agent

## Prerequisites
- Python 3.8 or higher
- Google Gemini API key (get from https://makersuite.google.com/app/apikey)

## Installation Steps

1. **Navigate to the project directory**
   ```bash
   cd C:\Users\navan\Downloads\001
   ```

2. **Install required packages**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   - Copy `.env.example` to `.env`:
     ```bash
     copy .env.example .env
     ```
   - Edit `.env` and replace `your_gemini_api_key_here` with your actual Google Gemini API key

4. **Start the FastAPI server**
   ```bash
   uvicorn main:app --reload
   ```

5. **Access the API**
   - The server will start at `http://localhost:8000`
   - Interactive API docs available at `http://localhost:8000/docs`

## Testing the Endpoint

You can test the `/scout` endpoint using:

### Using curl:
```bash
curl -X 'POST' \
  'http://localhost:8000/scout' \
  -H 'Content-Type: application/json' \
  -d '{
    "text": "We are looking for a Senior Backend Engineer with 4+ years of experience in Python, Django, REST APIs, and AWS. The role involves designing scalable microservices and mentoring junior developers."
  }'
```

### Using Python requests:
```python
import requests
import json

url = "http://localhost:8000/scout"
payload = {
    "text": "Senior Backend Engineer position requiring Python, Django, AWS, and 4+ years experience."
}
headers = {"Content-Type": "application/json"}

response = requests.post(url, json=payload, headers=headers)
print(response.json())
```

## Expected Output
The API returns a JSON object with a `results` array containing candidates ranked by their final score (Match × 0.7 + Interest × 0.3). Each candidate includes:
- Match score (0-100) with one-sentence reasoning
- Interest score (0-100) with one-sentence reasoning  
- Final score
- Generated outreach message
- Simulated candidate response

## Notes
- The first run may take a moment as the LLM processes the job description
- Candidate responses are simulated based on their availability and skills match
- For best results, use detailed job descriptions with specific skills and experience requirements