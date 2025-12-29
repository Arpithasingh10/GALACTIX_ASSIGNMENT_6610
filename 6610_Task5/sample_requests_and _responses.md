## Sample API Request

POST /analyze-feedback

Request Body:
```json
{
  "text": "The teaching is good but the workload is stressful."
}


{
  "text": "The course content is excellent and well structured."
}

```

## Sample API Responses

{
  "feedback": "The teaching is good but the workload is stressful.",
  "sentiment": "Negative",
  "score": -1
}


{
  "feedback": "The course content is excellent and well structured.",
  "sentiment": "Positive",
  "score": 1
}
