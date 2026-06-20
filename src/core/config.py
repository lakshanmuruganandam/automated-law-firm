from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Automated Law Firm Swarm"
    environment: str = "production"
    compliance_strictness: float = 0.99
    
    class Config:
        env_file = ".env"

settings = Settings()
