from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

from programador import Programadores
from habilidade import Habilidades

engine = create_engine('sqlite:///:memory:', echo=True)
db_session = scoped_session(sessionmaker(autocommit=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()


class Programadores_Habilidades(Base):
    __tablename__ = 'programadores_habilidades'

    programadores_id = Column(Integer, ForeignKey('programadores.id'), primary_key=True)
    programador_id = relationship("Programadores", back_populates='habilidades')

    habilidades_nome = Column(String, ForeignKey('habilidades.nome'))
    habilidade_nome = relationship("Habilidades", back_populates='programadores')

    def __repr__(self):
        return (f""" \n \t Programadores_Habilidades:
                \t \t Programador ID: {self.programadores_id} \n,
                \t \t Habilidades   : {self.habilidades_nome} >""")

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