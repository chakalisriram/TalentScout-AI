# AI-Powered Talent Scouting & Engagement Agent

A prototype for the Catalyst AI Hackathon by Deccan AI that takes a Job Description (JD) as input, discovers matching candidates, engages them conversationally (simulated), and outputs a ranked shortlist scored on Match Score and Interest Score.

## Files

- `candidates.json`: 10 diverse mock candidate profiles
- `main.py`: FastAPI backend with LangChain and Gemini 1.5 Flash implementation
- `requirements.txt`: Python dependencies
- `.env.example`: Example environment variables
- `EXPLAINABILITY.md`: Detailed explanation of the explainability implementation

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