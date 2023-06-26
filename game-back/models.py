from sqlalchemy import Column, Integer, String, SmallInteger, Date, ForeignKey, Table, DateTime
from sqlalchemy.orm import relationship
from database import Base


class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100))
    email = Column(String(150), unique=True, index=True)
    senha = Column(String(255))
    salas = relationship("Sala", back_populates="usuario")
    salas_participantes = relationship("Sala", secondary="participantes", back_populates="usuarios")
    
class Sala(Base):
    __tablename__ = 'salas'

    id = Column(Integer, primary_key=True, index=True)
    id_usuario = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    id_jogo = Column(Integer, ForeignKey("jogos.id"), nullable=False)
    nome = Column(String(100))
    descricao = Column(String(100))
    hora = Column(DateTime)
    usuario = relationship("Usuario", back_populates="salas")
    usuarios = relationship("Usuario", secondary="participantes", back_populates="salas_participantes")
    jogo = relationship("Jogo", back_populates="salas")
    
class Jogo(Base):
    __tablename__ = 'jogos'
    
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100))
    salas = relationship("Sala", back_populates="jogo")

participantes = Table('participantes', Base.metadata,
    Column('id_usuario', ForeignKey('usuarios.id'), primary_key=True),
    Column('id_sala', ForeignKey('salas.id'), primary_key=True)
)
