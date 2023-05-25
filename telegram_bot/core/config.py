from pydantic import BaseSettings


class Settings(BaseSettings):
    BOT_TOKEN: str
    WEB_APP_URL: str

    class Config:
        case_sensitive = True


settings = Settings()
