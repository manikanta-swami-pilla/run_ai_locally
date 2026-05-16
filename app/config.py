from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    OLLAMA_URL: str = "http://ollama:11434"
    DEFAULT_MODEL: str = "llama3.2"
    APP_ENV: str = "development"

    class Config:
        env_file = ".env"


settings = Settings()
