from pydantic import BaseModel, EmailStr
from typing import Optional


class UsuarioBase(BaseModel):
    nome: str
    email: EmailStr


class UsuarioCreate(UsuarioBase):
    senha: str


class Usuario(UsuarioBase):
    id_usuario: int
    data_criacao: str
    data_alteracao: str

    class Config:
        from_attributes = True


# Schemas para autenticação
class UsuarioLogin(BaseModel):
    email: EmailStr
    senha: str
