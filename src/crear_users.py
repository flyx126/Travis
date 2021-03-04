import os
from sqlalchemy.ext.automap import automap_base
from sqlalchemy import create_engine


engine = create_engine(f'postgresql://postgres:12345@localhost:5432/Dashboard-Toscalia')
engine.connect()

engine.execute("DROP TABLE IF EXISTS users")
engine.execute("CREATE TABLE users( id SERIAL ,nombre VARCHAR(20), apellido VARCHAR(20), username VARCHAR(10), password VARCHAR(10))")
engine.execute("INSERT INTO users (nombre,apellido,username,password) VALUES ('admin','admin','admin','admin')")
engine.execute("INSERT INTO users (nombre,apellido,username,password) VALUES ('Mauricio','Montenegro','Mauricio',12345)")