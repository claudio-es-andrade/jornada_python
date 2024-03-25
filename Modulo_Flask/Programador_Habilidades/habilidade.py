from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import  scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import  declarative_base

engine = create_engine('sqlite:///programador_Habilidade.db', echo=True)
db_session = scoped_session(sessionmaker(autocommit=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

class Habilidades(Base):
    __tablename__='habilidades'
    id = Column(Integer)
    nome = Column(String(40), primary_key=True, index=True)

    def __repr__(self):
        return (f""" \n \t Habilidades:
                \t \t Nome: {self.nome} >""" )

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