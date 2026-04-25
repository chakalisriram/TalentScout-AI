import json
import random

skills = ["Python", "React", "FastAPI", "SQL", "Docker", "Node.js", "LangChain", "PyTorch", "Solidity"]
names = ["Aarav", "Priya", "John", "Sarah", "Li", "Carlos", "Elena", "Anish", "Meera", "David"]

def generate():
    data = []
    for i in range(100):
        data.append({
            "name": f"{random.choice(names)} {random.choice(['Sharma', 'Verma', 'Smith', 'Lee', 'Gupta'])}",
            "skills": random.sample(skills, k=random.randint(2, 4)),
            "availability": random.choice(["Immediate", "2 Weeks", "1 Month"])
        })
    with open("candidates.json", "w") as f:
        json.dump(data, f, indent=4)
    print("Database Created!")

generate()