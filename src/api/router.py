from fastapi import APIRouter
from src.models.legal import ContractParams, DraftOutput
from src.services.agent import LegalAgentSwarm

api_router = APIRouter()
swarm = LegalAgentSwarm()

@api_router.post("/draft/contract", response_model=dict)
async def draft_contract(params: ContractParams):
    draft = await swarm.draft_contract(params)
    return {
        "status": "success", 
        "document": draft.model_dump()
    }
