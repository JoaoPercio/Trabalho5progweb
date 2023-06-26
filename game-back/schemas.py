from datetime import datetime
from typing import List  
from pydantic import BaseModel

class UsuarioBase(BaseModel):
    nome: str
    email: str
class UsuarioCreate(UsuarioBase):
    senha: str
class Usuario(UsuarioBase):
    id: int
    class Config:
        orm_mode = True
class PaginatedUsuario(BaseModel):
    limit: int
    offset: int
    data: List[Usuario]

class JogoBase(BaseModel):
    nome: str
class JogoCreate(JogoBase):
    pass
class Jogo(JogoBase):
    id: int
    class Config:
        orm_mode = True
class PaginatedJogo(BaseModel):
    limit: int
    offset: int
    data: List[Jogo]

class SalaBase(BaseModel):
    id_usuario:int
    id_jogo:int
    nome: str
    descricao:str
    hora: datetime
class SalaCreate(SalaBase):
    usuario_ids: List[int] = []
    pass
class Sala(SalaBase):
    id: int
    usuario: Usuario = {}
    jogo: Jogo = {}
    usuarios: List[Usuario] = []
    class Config:
        orm_mode = True
class PaginatedSala(BaseModel):
    limit: int
    offset: int
    data: List[Sala]

class UsuarioLoginSchema(BaseModel):
    email: str
    senha: str
    class Config:
        schema_extra = {
            "example": {
            "email": "x@x.com",
            "senha": "pass"
            }
        }

