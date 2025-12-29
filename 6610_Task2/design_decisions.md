## Design Decisions – Backend API (Task 2)

### Data Storage Decision
For this task, employee data is stored in an in-memory data structure
(a Python list). This means that the data exists only while the FastAPI
server is running and is not written to a file or database.

### Reason for Choosing In-Memory Storage
The primary goal of this task is to demonstrate backend API design,
request handling, and response behavior rather than database integration.
Using in-memory storage keeps the implementation simple, lightweight,
and easy to test. It also avoids additional complexity such as database
setup, configuration, and connectivity.

This approach allows faster development and helps focus on understanding
API fundamentals such as routing, validation, and error handling.

### How Data Is Stored
When a POST request is sent to the `/data` endpoint, the validated request
data is converted into a Python dictionary and appended to an in-memory
list. When a GET request is made to `/data`, the API returns all records
currently stored in this list.

### Limitations of This Approach
Since the data is stored in memory, it is lost when the server restarts.
This approach is not suitable for production systems where data
persistence is required.

### Future Scalability
For real-world or production use, the in-memory storage can be replaced
with a persistent database such as SQLite, PostgreSQL, or MongoDB. This
can be done without changing the API endpoints, making the design easily
extensible.
