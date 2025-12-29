from fastapi import FastAPI
from pydantic import BaseModel
import asyncio

app = FastAPI()

# -------- Data Model --------
class Feedback(BaseModel):
    text: str

# -------- Simple AI Simulation (async) --------
async def analyze_sentiment(text: str):
    await asyncio.sleep(1)  # async AI processing simulation

    text_lower = text.lower()

    # Rule-based fallback logic
    negative_keywords = ["stress", "overload", "unfair", "poor"]

    for word in negative_keywords:
        if word in text_lower:
            return "Negative"

    if "good" in text_lower or "excellent" in text_lower:
        return "Positive"

    return "Neutral"

# -------- Scoring Logic --------
def sentiment_score(sentiment: str):
    scores = {
        "Positive": 1,
        "Neutral": 0,
        "Negative": -1
    }
    return scores[sentiment]

# -------- API Endpoint --------
@app.post("/analyze-feedback")
async def analyze_feedback(feedback: Feedback):
    sentiment = await analyze_sentiment(feedback.text)
    score = sentiment_score(sentiment)

    return {
        "feedback": feedback.text,
        "sentiment": sentiment,
        "score": score
    }
