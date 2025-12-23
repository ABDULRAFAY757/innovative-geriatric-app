from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    MONGODB_URL: str
    DATABASE_NAME: str = "medical_app"

    class Config:
        env_file = ".env"

settings = Settings()
