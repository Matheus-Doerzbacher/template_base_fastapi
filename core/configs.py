from pydantic_settings import BaseSettings
from sqlalchemy.ext.declarative import declarative_base
from typing import ClassVar
from sqlalchemy.orm import DeclarativeBase


class Settings(BaseSettings):
    """
    Configurações gerais da aplicação
    """

    PROJECT_NAME: str = "API Template Base"
    API_V1_STR: str = "/api/v1"
    DB_URL: str = (
        "postgresql+asyncpg://[USUARIO]:[SENHA]@[HOST]:[PORTA]/[NOME_DO_BANCO]"
    )
    DBBaseModel: ClassVar[DeclarativeBase] = declarative_base()

    """
    import secrets

    token: str = secrets.token_urlsafe(32)
    """
    JWT_SECRET: str = "[NOVA_CHAVE_JWT]"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7  # 7 dias

    class Config:
        case_sensitive = True


settings: Settings = Settings()
