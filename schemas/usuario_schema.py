from pydantic import BaseModel, EmailStr
from typing import Optional


class UsuarioBase(BaseModel):
    nome: str
    email: EmailStr
    api_status: str
    data_criacao: str
    data_alteracao: str


class UsuarioCreate(UsuarioBase):
    senha: str


class UsuarioUpdate(UsuarioBase):
    nome: Optional[str] = None
    email: Optional[EmailStr] = None
    senha: Optional[str] = None
    api_status: Optional[str] = None
    data_alteracao: Optional[str] = None


class UsuarioInDB(UsuarioBase):
    id_usuario: int

    class Config:
        from_attributes = True


class Usuario(UsuarioInDB):
    pass


# Schemas para autenticação
class UsuarioLogin(BaseModel):
    email: EmailStr
    senha: str
