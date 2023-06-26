from fastapi import FastAPI, Depends, HTTPException, Body
from sqlalchemy.orm import Session
from exceptions import UsuarioException, JogoException, SalaException
from database import get_db, engine
import crud, models, schemas
from auth.auth_handler import signJWT
from auth.auth_bearer import JWTBearer
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine)
app = FastAPI()


# usuário
@app.get("/api/usuarios/{usuario_id}", dependencies=[Depends(JWTBearer())], response_model=schemas.Usuario)
def get_usuario_by_id(usuario_id: int, db: Session = Depends(get_db)):
    try:
        return crud.get_usuario_by_id(db, usuario_id)
    except UsuarioException as cie:
        raise HTTPException(**cie.__dict__)

@app.get("/api/usuarios", dependencies=[Depends(JWTBearer())], response_model=schemas.PaginatedUsuario)
def get_all_usuarios(db: Session = Depends(get_db), offset: int = 0, limit: int = 10):
    db_usuarios = crud.get_all_usuarios(db, offset, limit)
    response = {"limit": limit, "offset": offset, "data": db_usuarios}
    return response

@app.post("/api/usuarios", dependencies=[Depends(JWTBearer())], response_model=schemas.Usuario)
def create_usuario(usuario: schemas.UsuarioCreate, db: Session = Depends(get_db)):
    try:
        return crud.create_usuario(db, usuario)
    except UsuarioException as cie:
        raise HTTPException(**cie.__dict__)

@app.put("/api/usuarios/{usuario_id}", dependencies=[Depends(JWTBearer())], response_model=schemas.Usuario)
def update_usuario(usuario_id: int, usuario: schemas.UsuarioCreate, db: Session = Depends(get_db)):
    try:
        return crud.update_usuario(db, usuario_id, usuario)
    except UsuarioException as cie:
        raise HTTPException(**cie.__dict__)

@app.delete("/api/usuarios/{usuario_id}", dependencies=[Depends(JWTBearer())])
def delete_usuario_by_id(usuario_id: int, db: Session = Depends(get_db)):
    try:
        return crud.delete_usuario_by_id(db, usuario_id)
    except UsuarioException as cie:
        raise HTTPException(**cie.__dict__)

# login
@app.post("/api/signup", tags=["usuario"])
async def create_usuario_signup(usuario: schemas.UsuarioCreate = Body(...), db: Session = Depends(get_db)):
    try:
        crud.create_usuario(db, usuario)
        return signJWT(usuario.email)
    except UsuarioException as cie:
        raise HTTPException(**cie.__dict__)

# login
@app.post("/api/login", tags=["usuario"])
async def user_login(usuario: schemas.UsuarioLoginSchema = Body(...), db: Session = Depends(get_db)):
    if crud.check_usuario(db, usuario):
        return signJWT(usuario.email)
    return {
        "error": "E-mail ou senha incorretos!"
    }

#jogo
@app.get("/api/jogos/{jogo_id}", dependencies=[Depends(JWTBearer())], response_model=schemas.Jogo)
def get_jogo_by_id(jogo_id: int, db: Session = Depends(get_db)):
    try:
        return crud.get_jogo_by_id(db, jogo_id)
    except JogoException as cie:
        raise HTTPException(**cie.__dict__)

@app.get("/api/jogos", dependencies=[Depends(JWTBearer())], response_model=schemas.PaginatedJogo)
def get_all_jogos(db: Session = Depends(get_db), offset: int = 0, limit: int = 10):
    db_jogos = crud.get_all_jogos(db, offset, limit)
    response = {"limit": limit, "offset": offset, "data": db_jogos}
    return response

@app.post("/api/jogos", dependencies=[Depends(JWTBearer())], response_model=schemas.Jogo)
def create_jogo(jogo: schemas.JogoCreate, db: Session = Depends(get_db)):
    try:
        return crud.create_jogo(db, jogo)
    except JogoException as cie:
        raise HTTPException(**cie.__dict__)

@app.put("/api/jogos/{jogo_id}", dependencies=[Depends(JWTBearer())], response_model=schemas.Jogo)
def update_jogo(jogo_id: int, jogo: schemas.JogoCreate, db: Session = Depends(get_db)):
    try:
        return crud.update_jogo(db, jogo_id, jogo)
    except JogoException as cie:
        raise HTTPException(**cie.__dict__)

@app.delete("/api/jogos/{jogo_id}", dependencies=[Depends(JWTBearer())])
def delete_jogo_by_id(jogo_id: int, db: Session = Depends(get_db)):
    try:
        return crud.delete_jogo_by_id(db, jogo_id)
    except JogoException as cie:
        raise HTTPException(**cie.__dict__)

#sala
@app.post("/api/salas", dependencies=[Depends(JWTBearer())], response_model=schemas.Sala)
def create_sala(sala: schemas.SalaCreate, db: Session = Depends(get_db)):
    try:
        return crud.create_sala(db, sala)
    except SalaException as cie:
        raise HTTPException(**cie.__dict__)

@app.get("/api/salas/{sala_id}", dependencies=[Depends(JWTBearer())], response_model=schemas.Sala)
def get_sala_by_id(sala_id: int, db: Session = Depends(get_db)):
    try:
        return crud.get_sala_by_id(db, sala_id)
    except SalaException as cie:
        raise HTTPException(**cie.__dict__)

@app.get("/api/salas", dependencies=[Depends(JWTBearer())], response_model=schemas.PaginatedSala)
def get_all_salas(db: Session = Depends(get_db), offset: int = 0, limit: int = 10):
    db_salas = crud.get_all_salas(db, offset, limit)
    response = {"limit": limit, "offset": offset, "data": db_salas}
    return response

@app.put("/api/salas/{sala_id}", dependencies=[Depends(JWTBearer())], response_model=schemas.Sala)
def update_sala(sala_id: int, sala: schemas.SalaCreate, db: Session = Depends(get_db)):
    return crud.update_sala(db, sala_id, sala)

@app.delete("/api/salas/{sala_id}", dependencies=[Depends(JWTBearer())])
def delete_sala_by_id(sala_id: int, db: Session = Depends(get_db)):
    try:
        return crud.delete_sala_by_id(db, sala_id)
    except JogoException as cie:
        raise HTTPException(**cie.__dict__)

