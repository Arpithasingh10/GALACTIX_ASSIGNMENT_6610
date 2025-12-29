from pydantic import BaseModel
from typing import Optional

class Employee(BaseModel):
    age: Optional[int]
    attrition: Optional[str]
    department: Optional[str]
    job_role: Optional[str]
    monthly_income: Optional[float]
    years_at_company: Optional[int]
    work_life_balance: Optional[int]
    gender: Optional[str]
