from urllib.parse import quote_plus

from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, scoped_session, declarative_base

from model import Atividades

user, password, host, database = 'root', 'password', 'localhost', 'db'
encoded_password = quote_plus(password)
engine = create_engine(
    url=f'mysql+pymysql://{user}:{encoded_password}@{host}/{database}?charset=utf8')


connection = engine.connect()

table_name = 'atividades'

query = text(f'ALTER TABLE {table_name} ADD status ENUM("concluido","pendente") ;')
connection.execute(query)
connection.commit()
connection.close()
