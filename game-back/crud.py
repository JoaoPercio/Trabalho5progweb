from sqlalchemy.orm import Session
from exceptions import UsuarioAlreadyExistError, UsuarioNotFoundError, JogoNotFoundError, SalaNotFoundError
import bcrypt, models, schemas

# usuário
def get_usuario_by_id(db: Session, usuario_id: int):
    db_usuario = db.query(models.Usuario).get(usuario_id)
    if db_usuario is None:
        raise UsuarioNotFoundError
    return db_usuario

def get_all_usuarios(db: Session, offset: int, limit: int):
    return db.query(models.Usuario).offset(offset).limit(limit).all()

def get_usuario_by_email(db: Session, usuario_email: str):
    return db.query(models.Usuario).filter(models.Usuario.email == usuario_email).first()

def create_usuario(db: Session, usuario: schemas.UsuarioCreate):
    db_usuario = get_usuario_by_email(db, usuario.email)
    # O parâmetro rounds do gensalt determina a complexidade. O padrão é 12.
    usuario.senha = bcrypt.hashpw(usuario.senha.encode('utf8'), bcrypt.gensalt())
    if db_usuario is not None:
        raise UsuarioAlreadyExistError
    db_usuario = models.Usuario(**usuario.dict())
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

def update_usuario(db: Session, usuario_id: int, usuario: schemas.UsuarioCreate):
    db_usuario = get_usuario_by_id(db, usuario_id)
    db_usuario.nome = usuario.nome
    db_usuario.email = usuario.email
    if usuario.senha != "":
        # O parâmetro rounds do gensalt determina a complexidade. O padrão é 12.
        db_usuario.senha = bcrypt.hashpw(usuario.senha.encode('utf8'), bcrypt.gensalt())
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

def delete_usuario_by_id(db: Session, usuario_id: int):
    db_usuario = get_usuario_by_id(db, usuario_id)
    db.delete(db_usuario)
    db.commit()
    return

def check_usuario(db: Session, usuario: schemas.UsuarioLoginSchema):
    db_usuario = db.query(models.Usuario).filter(models.Usuario.email == usuario.email).first()
    if db_usuario is None:
        return False
    return bcrypt.checkpw(usuario.senha.encode('utf8'), db_usuario.senha.encode('utf8'))

#jogo

def get_all_jogos(db: Session, offset: int, limit: int):
    return db.query(models.Jogo).offset(offset).limit(limit).all()

def get_jogo_by_id(db: Session, jogo_id: int):
    db_jogo = db.query(models.Jogo).get(jogo_id)
    if db_jogo is None:
        raise JogoNotFoundError
    return db_jogo

def create_jogo(db: Session, jogo: schemas.JogoCreate):
    db_jogo = models.Jogo(**jogo.dict())
    db.add(db_jogo)
    db.commit()
    db.refresh(db_jogo)
    return db_jogo

def update_jogo(db: Session, jogo_id: int, jogo: schemas.JogoCreate):
    db_jogo = get_jogo_by_id(db, jogo_id)
    db_jogo.nome = jogo.nome
    db.commit()
    db.refresh(db_jogo)
    return db_jogo

def delete_jogo_by_id(db: Session, jogo_id: int):
    db_jogo = get_jogo_by_id(db, jogo_id)
    db.delete(db_jogo)
    db.commit()
    return

#sala

def get_all_salas(db: Session, offset: int, limit: int):
    return db.query(models.Sala).offset(offset).limit(limit).all()

def get_sala_by_id(db: Session, sala_id: int):
    db_sala = db.query(models.Sala).get(sala_id)
    if db_sala is None:
        raise SalaNotFoundError
    return db_sala

def create_sala(db: Session, sala: schemas.SalaCreate):
    get_usuario_by_id(db, sala.id_usuario)
    get_jogo_by_id(db, sala.id_jogo)
    db_sala = models.Sala(id_usuario=sala.id_usuario, id_jogo=sala.id_jogo, nome=sala.nome, descricao=sala.descricao, hora=sala.hora)
    if (usuarios := db.query(models.Usuario).filter(models.Usuario.id.in_(sala.usuario_ids))).count() == len(sala.usuario_ids):
        db_sala.usuarios.extend(usuarios)
    else:
        raise UsuarioNotFoundError
    db.add(db_sala)
    db.commit()
    db.refresh(db_sala)
    return db_sala


def update_sala(db: Session, sala_id: int, sala: schemas.SalaCreate):
    db_sala = get_sala_by_id(db, sala_id)
    db_sala.nome = sala.nome
    db_sala.descricao = sala.descricao
    db_sala.hora = sala.hora
    db.commit()
    db.refresh(db_sala)
    return db_sala

def delete_sala_by_id(db: Session, sala_id: int):
    db_sala = get_sala_by_id(db, sala_id)
    db.delete(db_sala)
    db.commit()
    return

