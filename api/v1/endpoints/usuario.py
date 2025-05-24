from sqlite3 import IntegrityError
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import JSONResponse

from sqlalchemy.ext.asyncio import AsyncSession
from core.auth import autenticar, criar_token_acesso
from core.security import gerar_hash_senha

router = APIRouter(prefix="/usuarios", tags=["usuarios"])

from core.deps import get_current_user, get_session

from models.usuario_model import UsuarioModel
from schemas.usuario_schema import Usuario, UsuarioCreate, UsuarioUpdate
from datetime import datetime


# GET Usuario Logado
@router.get("/logado", response_model=Usuario)
def get_logado(usuario_logado: UsuarioModel = Depends(get_current_user)):
    return usuario_logado


@router.post("/login")
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: AsyncSession = Depends(get_session),
):
    print(form_data.username, form_data.password)
    usuario = await autenticar(form_data.username, form_data.password, db)

    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Dados de acesso inválidos",
        )

    return JSONResponse(
        content={
            "access_token": criar_token_acesso(sub=usuario.id_usuario),
            "token_type": "Bearer",
        },
    )


# POST Usuario
@router.post("/", response_model=Usuario, status_code=status.HTTP_201_CREATED)
async def post_usuario(
    usuario: UsuarioCreate,
    db: AsyncSession = Depends(get_session),
):
    try:
        async with db as session:
            usuario = UsuarioModel(
                nome=usuario.nome,
                email=usuario.email,
                senha=gerar_hash_senha(usuario.senha),
                data_criacao=datetime.now().isoformat(),
                data_alteracao=datetime.now().isoformat(),
            )

            session.add(usuario)
            await session.commit()
            return usuario

    except IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail="Usuário já cadastrado",
        )


# PUT Usuario
@router.put("/{usuario_id}", response_model=Usuario)
async def put_usuario(
    usuario_id: int,
    usuario: UsuarioUpdate,
    db: AsyncSession = Depends(get_session),
    usuario_logado: UsuarioModel = Depends(get_current_user),
):
    if usuario_logado.id != usuario_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Não é possível atualizar o usuário logado",
        )

    async with db as session:
        usuario_bd: UsuarioModel = await session.get(UsuarioModel, usuario_id)

        if not usuario_bd:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Usuário não encontrado",
            )

        # Atualiza apenas os campos permitidos
        for key, value in usuario.model_dump(exclude_unset=True).items():
            if key != "senha" and key != "data_alteracao":
                setattr(usuario_bd, key, value)

        if usuario.senha:
            usuario_bd.senha = gerar_hash_senha(usuario.senha)

        usuario_bd.data_alteracao = datetime.now().isoformat()

        await session.commit()
        await session.refresh(usuario_bd)
        return usuario_bd


# DELETE Usuario
@router.delete("/{usuario_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_usuario(
    usuario_id: int,
    db: AsyncSession = Depends(get_session),
    usuario_logado: UsuarioModel = Depends(get_current_user),
):
    if usuario_logado.id != usuario_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Não é possível deletar o usuário logado",
        )
    async with db as session:
        usuario_bd: UsuarioModel = await session.get(UsuarioModel, usuario_id)

        if not usuario_bd:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Usuário não encontrado",
            )

        await session.delete(usuario_bd)
        await session.commit()
