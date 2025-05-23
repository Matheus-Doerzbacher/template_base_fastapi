# Template Base API

Este é um projeto template base para desenvolvimento de APIs em Python, utilizando FastAPI e PostgreSQL.

## 🚀 Tecnologias

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy (ORM)
- Pydantic
- JWT para autenticação

## 📋 Pré-requisitos

- Python 3.8+
- PostgreSQL
- pip (gerenciador de pacotes Python)

## 🔧 Configuração do Ambiente

1. Clone o repositório:
```bash
git clone [URL_DO_REPOSITÓRIO]
cd [NOME_DO_PROJETO]
```

2. Crie um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
.\venv\Scripts\activate  # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Configure o banco de dados:
   - Crie um banco de dados PostgreSQL
   - Ajuste as configurações de conexão no arquivo `core/configs.py`:
     ```python
     DB_URL: str = "postgresql+asyncpg://[USUARIO]:[SENHA]@[HOST]:[PORTA]/[NOME_DO_BANCO]"
     ```

5. Configure as variáveis de ambiente:
   - Gere uma nova chave JWT_SECRET (recomendado para produção):
     ```python
     import secrets
     token = secrets.token_urlsafe(32)
     ```
   - Atualize o JWT_SECRET no arquivo `core/configs.py`

## ⚙️ Configurações Personalizáveis

No arquivo `core/configs.py`, você pode personalizar:

- `PROJECT_NAME`: Nome do seu projeto
- `API_V1_STR`: Prefixo da API
- `DB_URL`: URL de conexão com o banco de dados
- `JWT_SECRET`: Chave secreta para tokens JWT
- `ACCESS_TOKEN_EXPIRE_MINUTES`: Tempo de expiração dos tokens (padrão: 7 dias)

## 🏃‍♂️ Criando as tabelas do Projeto

```bash
python criar_tabelas.py
```

Isso irá criar as tabelas no banco.

## 🏃‍♂️ Executando o Projeto

```bash
python main.py
```

O servidor estará disponível em `http://localhost:8000`

## 📚 Documentação

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## 🔐 Segurança

- Nunca compartilhe ou comite o JWT_SECRET
- Em ambiente de produção, use variáveis de ambiente para configurações sensíveis
- Mantenha as dependências atualizadas