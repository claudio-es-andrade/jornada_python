from urllib.parse import quote_plus

from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, scoped_session, declarative_base

from model import Usuarios

user, password, host, database = 'root', 'rootpassword', 'localhost', 'db'
encoded_password = quote_plus(password)
engine = create_engine(
    url=f'mysql+mysqlconnector://{user}:{encoded_password}@{host}/{database}?charset=utf8' )


connection = engine.connect()

table_name = 'usuarios'

query = text(f'ALTER TABLE {table_name} ADD ativo ENUM("ativo","desativado") ;')
connection.execute(query)
connection.commit()
connection.close()
