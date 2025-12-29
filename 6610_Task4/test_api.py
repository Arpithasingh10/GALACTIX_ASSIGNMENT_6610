import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.responses.create(
    model="gpt-5-nano",
    input="Write one sentence about artificial intelligence."
)

print(response.output_text)
