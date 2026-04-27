from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

leads = []

class Lead(BaseModel):
    id: int
    name: str
    email: str
    status: str = "new"
    is_converted: bool = False

@app.get("/leads")
def get_leads():
    return leads

@app.post("/leads")
def add_lead(lead: Lead):
    leads.append(lead.dict())
    return {"message": "Lead added"}

@app.put("/leads/{lead_id}")
def update_lead(lead_id: int, data: dict):
    for lead in leads:
        if lead["id"] == lead_id:
            lead["status"] = data.get("status", lead["status"])
            lead["is_converted"] = lead["status"] == "closed"
    return {"message": "Updated"}

@app.get("/dashboard")
def dashboard():
    total = len(leads)
    converted = sum(1 for l in leads if l["is_converted"])
    conversion_rate = (converted / total * 100) if total > 0 else 0
    return {
        "total": total,
        "converted": converted,
        "conversion_rate": conversion_rate
    }


