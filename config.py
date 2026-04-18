# Python 3.12+
from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """Configurações centralizadas do sistema JARVIS."""
    JARVIS_NAME: str = "jarvis"
    OPENAI_API_KEY: str | None = None
    
    # Caminhos de Aplicativos (Ajuste conforme seu SO)
    VS_CODE_PATH: str = "code" # Assume que está no PATH
    SLACK_PATH: str | None = None
    
    # Sensibilidade de som
    CLAP_THRESHOLD: float = 0.15 # Ajuste conforme o microfone
    
    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()