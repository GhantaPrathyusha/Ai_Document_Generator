from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str

    DATABASE_URL: str | None = None   # <-- ADD THIS LINE

    JWT_SECRET: str
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    GOOGLE_API_KEY: str
    GEMINI_MODEL: str = "models/gemini-2.5-flash"

    EXPORT_DIR: str = "exports"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()

# Build DATABASE_URL dynamically
settings.DATABASE_URL = (
    f"mysql+pymysql://{settings.DB_USER}:{settings.DB_PASSWORD}"
    f"@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}"
)
