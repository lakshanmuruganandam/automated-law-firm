from pydantic import BaseModel, Field

class ContractParams(BaseModel):
    contract_type: str = Field(..., description="e.g., NDA, Employment, SaaS")
    parties: list[str] = Field(..., description="Entities involved")
    jurisdiction: str = Field(..., description="Legal jurisdiction governing the contract")

class DraftOutput(BaseModel):
    title: str
    content: str
    risk_score: float
