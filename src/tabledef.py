from src.db import Db
from src.log import log
from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref


db=Db()
engine = db.create_session()
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    nombre = Column(String(50))
    apellido = Column(String(50))
    username = Column(String(50))
    password = Column(String(50))

    def __init__(self, nombre, apellido,username, password):
        self.nombre = nombre
        self.apellido= apellido
        self.username=username
        self.password=password

    def __repr__(self):
        return "<User(nombre='%s', apellido='%s', username='%s', password='%s' )>" % (
        self.nombre, self.apellido, self.username, self.password)


# Base.metadata.create_all(engine)


