from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Grant Threshold Validator API")

# Define what a "Grant Application" looks like
class GrantApplication(BaseModel):
    organization_name: str
    requested_amount: float
    project_summary: str

@app.post("/validate-grant/")
def validate_grant(grant: GrantApplication):
    # The logic you proved you could do yesterday!
    if grant.requested_amount > 50000:
        return {
            "status": "FLAGGED FOR REVIEW",
            "reason": f"Requested amount ${grant.requested_amount:,.2f} exceeds the $50,000 threshold.",
            "requires_manual_audit": True
        }
    else:
        return {
            "status": "APPROVED",
            "reason": f"Requested amount ${grant.requested_amount:,.2f} is within automated limits.",
            "requires_manual_audit": False
        }