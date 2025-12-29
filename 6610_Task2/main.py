from fastapi import FastAPI, HTTPException
from models import Employee
from storage import add_record, get_all_records

app = FastAPI(title="HR Attrition API")


# Health check endpoint
@app.get("/health")
def health_check():
    return {"status": "OK"}


# POST /data → add employee record
@app.post("/data", status_code=201)
def create_data(employee: Employee):
    try:
        add_record(employee.dict())
        return {"message": "Record added successfully"}
    except Exception:
        raise HTTPException(status_code=500, detail="Failed to add record")


# GET /data → fetch all records
@app.get("/data")
def read_data():
    records = get_all_records()
    if not records:
        raise HTTPException(status_code=404, detail="No data found")
    return records
@app.get("/")
def root():
    return {"message": "HR Attrition API is running"}
