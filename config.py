import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    # OpenAI Configuration
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    GPT_MODEL = os.getenv("GPT_MODEL", "gpt-4-1106-preview")  # Default to GPT-4 Turbo
    
    # PostgreSQL Configuration
    POSTGRES_URI = os.getenv("POSTGRES_URI")
    
    # Server Configuration
    SERVER_HOST = os.getenv("SERVER_HOST", "[::]")  # Default to all interfaces
    SERVER_PORT = int(os.getenv("SERVER_PORT", "50051"))  # Default gRPC port
    
    # AI Service Configuration
    MAX_TOKENS = int(os.getenv("MAX_TOKENS", "4000"))
    TEMPERATURE = float(os.getenv("TEMPERATURE", "0.7"))
    
    @classmethod
    def validate(cls):
        """Validate required configuration variables."""
        if not cls.OPENAI_API_KEY:
            raise ValueError("OPENAI_API_KEY must be set in environment variables")
        if not cls.POSTGRES_URI:
            raise ValueError("POSTGRES_URI must be set in environment variables")

# Validate configuration on import
Config.validate() 