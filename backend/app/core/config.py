class Settings:
    DATABASE_URL = "sqlite:///./dms.db"
    SECRET_KEY = "supersecretkey"
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_HOURS = 2

settings = Settings()