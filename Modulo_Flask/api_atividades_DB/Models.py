from urllib.parse import quote_plus
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Enum, text
from sqlalchemy.orm import sessionmaker, scoped_session, declarative_base, relationship
from sqlalchemy.exc import SQLAlchemyError

# Database configuration
user = 'root'
password = 'password'
host = 'localhost'
database = 'db'
encoded_password = quote_plus(password)
engine = create_engine(
    url=f'mysql+pymysql://{user}:{encoded_password}@{host}/{database}?charset=utf8'
)

# Session setup
Session = scoped_session(sessionmaker(bind=engine))
db_session = Session()

# Declarative base
Base = declarative_base()

# Define the Pessoas model
class Pessoas(Base):
    __tablename__ = 'pessoas'
    id = Column(Integer, primary_key=True)
    nome = Column(String(40), index=True)
    idade = Column(Integer)

    def __repr__(self):
        return f'<Pessoa: {self.nome}>'

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

# Define the Atividades model
class Atividades(Base):
    __tablename__ = 'atividades'
    id = Column(Integer, primary_key=True)
    nome = Column(String(80))
    pessoa_id = Column(Integer, ForeignKey('pessoas.id'))
    pessoa = relationship("Pessoas")

    def __repr__(self):
        return f'<Atividades: {self.nome}>'

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

# Initialize the database and create tables
def init_db():
    Base.metadata.create_all(bind=engine)

# Add the new ENUM column to the 'atividades' table
def add_enum_column():
    connection = engine.connect()
    try:
        table_name = 'atividades'
        query = text(f'ALTER TABLE {table_name} ADD COLUMN status ENUM("concluido", "pendente");')
        connection.execute(query)
        print("Column added successfully.")
    except SQLAlchemyError as e:
        print(f"An error occurred: {e}")
    finally:
        connection.close()

if __name__ == '__main__':
    init_db()
    add_enum_column()
