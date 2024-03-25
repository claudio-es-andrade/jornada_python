from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import  scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import  declarative_base

engine = create_engine('sqlite:///programador_Habilidade.db', echo=True)
db_session = scoped_session(sessionmaker(autocommit=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

class Programadores(Base):
    __tablename__='programadores'
    id = Column(Integer, primary_key=True)
    nome = Column(String(40), index=True)
    idade = Column(Integer)
    email = Column(String(40))

    def __repr__(self):
        return (f""" \n \t Programadores:
                \t \t Nome: {self.nome}, \n 
                \t \t Idade: {self.idade}, \n,
                \t \t E-mail: {self.email}>""" )

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()


def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    init_db()