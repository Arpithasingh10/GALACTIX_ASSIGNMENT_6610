## Async vs Sync Performance Analysis

This experiment was conducted using FastAPI with one synchronous
endpoint implemented using time.sleep() and one asynchronous
endpoint implemented using asyncio.sleep().

For a single request, both synchronous and asynchronous endpoints
showed similar execution times of approximately 2 seconds, as no
concurrent processing was involved.

When 10 concurrent requests were sent to the synchronous endpoint
using PowerShell background jobs, the requests were processed
sequentially. Each request took about 2 seconds, resulting in a
total execution time of roughly 20–22 seconds.

In contrast, when 10 concurrent requests were sent to the asynchronous
endpoint, all requests were handled concurrently. Although each
request still took around 2 seconds individually, the overall
execution time remained close to 2–3 seconds.

The same behavior was also verified by opening multiple Swagger UI
tabs and triggering requests simultaneously.

This experiment demonstrates that asynchronous programming
significantly improves performance for concurrent and I/O-bound
operations, whereas synchronous execution blocks request handling
and increases total response time.

### Commands Used for Testing
## Start FastAPI server
uvicorn main:app --reload

## Single request testing

Synchronous endpoint

Invoke-WebRequest http://127.0.0.1:8000/sync -UseBasicParsing

## Asynchronous endpoint

Invoke-WebRequest http://127.0.0.1:8000/async -UseBasicParsing

10 concurrent requests (PowerShell background jobs)

## Synchronous

1..10 | ForEach-Object { Start-Job { Invoke-WebRequest http://127.0.0.1:8000/sync -UseBasicParsing } }
Get-Job
Receive-Job *

## Asynchronous

1..10 | ForEach-Object { Start-Job { Invoke-WebRequest http://127.0.0.1:8000/async -UseBasicParsing } }
Get-Job
Receive-Job *

### Alternative testing method

Open multiple browser tabs at
http://127.0.0.1:8000/docs

Trigger the same endpoint from different tabs simultaneously

Observe execution time behavior in API responses

## Observation

Sync endpoint: requests executed sequentially, total time increased linearly

Async endpoint: requests executed concurrently, total time remained nearly constant

Execution times were observed directly from API responses