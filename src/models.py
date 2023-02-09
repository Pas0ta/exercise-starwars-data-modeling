import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    apellido = Column(String(250), nullable=False)
    correo = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    nombre_usuario = Column(String(250), nullable=False)
    fecha_registro = Column(String(250), nullable=False)
    favusuario = relationship('Favorito', backref='usuario', lazy=True)

class Personajes(Base):
    __tablename__ = 'personajes'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    cumpleaños = Column(String(250), nullable=False)
    altura = Column(String(250), nullable=False)
    peso = Column(String(250), nullable=False)
    nogenero = Column(String(250), nullable=False)
    color_pelo = Column(String(250), nullable=False)
    color_piel = Column(String(250), nullable=False)
    favpersonajes = relationship('Favorito', backref='personajes', lazy=True)

class Planetas(Base):
    __tablename__ = 'planetas'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    color = Column(String(250), nullable=False)
    tamaño = Column(String(250), nullable=False)
    poaicion = Column(String(250), nullable=False)
    clima = Column(String(250), nullable=False)
    gravedad = Column(String(250), nullable=False)
    rotacion = Column(String(250), nullable=False)
    orbita = Column(String(250), nullable=False)
    terreno = Column(String(250), nullable=False)
    poblacion = Column(String(250), nullable=False)
    favplanetas = relationship('Favoritos', backref='planetas', lazy=True)

    def to_dict(self):
        return {}

class Favorito(Base):
    __tablename__ = 'favorito'
    id = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, ForeignKey('usuario.id'),
        nullable=False)
    id_planetas = Column(Integer, ForeignKey('planetas.id'),
        nullable=False)
    personajes_id = Column(Integer, ForeignKey('personajes.id'),
        nullable=False)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
