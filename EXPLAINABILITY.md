# Explainability Implementation

The agent provides explainability at two key stages:

## 1. Match Score Explainability

In the `match_scorer_chain`, we prompt the LLM to:
- Provide a numerical match score (0-100)
- Give a one-sentence reasoning explaining the primary factor behind that score

Example output:
```json
{
  "match_score": 85,
  "match_reasoning": "Strong skills match with 4 years of Python/Django experience aligning well with the required backend technologies."
}
```

## 2. Interest Score Explainability

In the `interest_scorer_chain`, we prompt the LLM to:
- Analyze the simulated candidate response
- Provide a numerical interest score (0-100)
- Give a one-sentence reasoning explaining the primary factor behind that score

Example output:
```json
{
  "interest_score": 90,
  "interest_reasoning": "Candidate expresses immediate availability and enthusiasm about the opportunity, indicating strong interest."
}
```

## How to Display in Frontend

Each candidate result includes:
- `match_score`: Numerical score (0-100)
- `match_reasoning`: One-sentence explanation
- `interest_score`: Numerical score (0-100)
- `interest_reasoning`: One-sentence explanation
- `final_score`: Weighted combination (Match × 0.7 + Interest × 0.3)

The frontend can display these as:
- Score badges with tooltips showing the reasoning
- Expandable sections for detailed explanations
- Color-coded indicators (green/yellow/red) based on score ranges

This approach satisfies the judging criteria for "Quality of core agent/reasoning" by providing transparent, interpretable scoring that recruiters can trust and act upon.