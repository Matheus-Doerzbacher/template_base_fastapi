from core.configs import settings
from sqlalchemy import Column, Integer, String, Index


class UsuarioModel(settings.DBBaseModel):

    __tablename__ = "usuarios"

    id_usuario: int = Column(Integer, primary_key=True, autoincrement=True)
    nome: str = Column(String(256), nullable=False, index=True)
    email: str = Column(String(256), nullable=False, unique=True, index=True)
    senha: str = Column(String(256), nullable=False)
    api_status = Column(String(256), nullable=False)
    data_criacao = Column(String(256), nullable=False)
    data_alteracao = Column(String(256), nullable=False)
