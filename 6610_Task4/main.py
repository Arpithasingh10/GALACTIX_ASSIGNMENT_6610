import os
import json
from datetime import datetime

# Try importing OpenAI
try:
    from openai import OpenAI
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    api_available = True
except:  # noqa: E722
    api_available = False


input_text = "The company culture is good, but the workload is stressful and deadlines are tight."

prompts = [
    "Analyze the sentiment of the following text and classify it as Positive, Negative, or Neutral.",
    "Determine the overall emotional tone of the text. Consider both positive and negative aspects before deciding.",
    "Classify the sentiment of the text into one word only: Positive, Negative, or Neutral."
]

mock_outputs = [
    "Neutral",
    "Mixed sentiment (neutral overall)",
    "Neutral"
]

results = []

for i, prompt in enumerate(prompts):
    timestamp = datetime.now().isoformat()

    if api_available:
        try:
            response = client.responses.create(
                model="gpt-5-nano",
                input=f"{prompt}\n\nText: {input_text}"
            )
            output = response.output_text
        except Exception:
            output = "API error: insufficient quota"
    else:
        output = mock_outputs[i]

    results.append({
        "timestamp": timestamp,
        "prompt_version": f"Prompt {i+1}",
        "prompt": prompt,
        "input_text": input_text,
        "output": output
    })

with open("ai_results.json", "w") as f:
    json.dump(results, f, indent=4)

print("Results saved to ai_results.json")
