from fastapi import APIRouter
from pydantic import BaseModel

api_router = APIRouter()

class ContractParams(BaseModel):
    contract_type: str
    parties: list[str]
    jurisdiction: str

@api_router.post("/draft/contract")
async def draft_contract(params: ContractParams):
    # Triggers the drafting agent
    return {
        "status": "success", 
        "document": f"DRAFT {params.contract_type} between {', '.join(params.parties)} under the laws of {params.jurisdiction}."
    }
