import requests
import json
import time

def test_api():
    # Wait a moment for server to start
    time.sleep(2)
    
    url = "http://localhost:8000/scout"
    payload = {
        "text": "Senior Backend Engineer needing Python, Django, AWS, 4+ years experience"
    }
    headers = {"Content-Type": "application/json"}
    
    try:
        response = requests.post(url, json=payload, headers=headers)
        print("Status Code:", response.status_code)
        if response.status_code == 200:
            result = response.json()
            print("Success! Received response with", len(result.get('results', [])), "candidates")
            # Print first candidate details
            if result.get('results'):
                first = result['results'][0]
                print(f"Top candidate: {first['name']}")
                print(f"Match Score: {first['match_score']} - {first['match_reasoning']}")
                print(f"Interest Score: {first['interest_score']} - {first['interest_reasoning']}")
                print(f"Final Score: {first['final_score']}")
        else:
            print("Error:", response.text)
    except Exception as e:
        print("Error connecting to API:", str(e))

if __name__ == "__main__":
    test_api()