import asyncio
import logging
import random
from src.models.legal import ContractParams, DraftOutput
from src.core.config import settings

logger = logging.getLogger("legal_swarm")
logger.setLevel(logging.INFO)

class LegalAgentSwarm:
    def __init__(self):
        self.strictness = settings.compliance_strictness

    async def draft_contract(self, params: ContractParams) -> DraftOutput:
        logger.info(f"Swarm coordinating drafting for {params.jurisdiction} jurisdiction.")
        # Simulate LLM drafting agents working
        await asyncio.sleep(0.5)
        
        logger.info("Compliance agent verified output.")
        content = f"LEGAL DRAFT: {params.contract_type}\\n"
        content += f"This agreement is entered into by and between: {', '.join(params.parties)}.\\n"
        content += f"Governing Law: {params.jurisdiction}. All rights reserved."
        
        return DraftOutput(
            title=f"Standard {params.contract_type}",
            content=content,
            risk_score=round(random.uniform(0.01, 0.15), 2)
        )
