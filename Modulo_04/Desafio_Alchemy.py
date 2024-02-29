from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session
from sqlalchemy     import create_engine
from sqlalchemy     import func
from sqlalchemy     import inspect
from sqlalchemy     import Integer
from sqlalchemy     import Float
from sqlalchemy     import String
from sqlalchemy     import ForeignKey
from sqlalchemy     import Column
from sqlalchemy     import select


Base = declarative_base()

class Cliente(Base):
    __tablename__ = "cliente_account"

    #atributos

    id                             = Column(Integer, primary_key = True)
    nome                           = Column(String(100))
    cpf                            = Column(String(9))
    endereco                       = Column(String(200))

    conta                          = relationship(
        "Conta", back_populates="cliente", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"Cliente \n (id={self.id}, nome={self.nome}, cpf={self.cpf}, endereco={self.endereco})"

class Conta(Base):
    __tablename__ = "conta_account"

    # atributos
    id                             = Column(Integer, primary_key = True)       #auto_increment = True)
    tipo                           = Column(String(100))
    agencia                        = Column(String(100), nullable = False)
    num                            = Column(Integer)
    id_cliente                     = Column(Integer, ForeignKey("cliente_account.id"), nullable = False)
    saldo                          = Column(Float)

    cliente                        = relationship("Cliente", back_populates="conta")

    def __repr__(self):
        return f"Conta \n ( id={self.id}, tipo={self.tipo}, agencia={self.agencia}, num={self.num}, id_cliente={self.id_cliente}, saldo={self.saldo} )"

print(Cliente.__tablename__)
print(Conta.__tablename__)

# Conexão com o Banco de Dados
engine                             = create_engine("sqlite://")

#Criando as classes como tabelas no Banco de Dados
Base.metadata.create_all(engine)

# Depreciado - será removido na próxima atualização
# print(engine.table_names())

inspector_engine                   = inspect(engine)
print(inspector_engine.has_table("cliente_account"))

inspector_engine                   = inspect(engine)
print(inspector_engine.has_table("conta_account"))

print(inspector_engine.get_table_names())
print(inspector_engine.default_schema_name)

with Session(engine) as session:
    adriana                        = Cliente(
        nome                       = "Adriana Ramos",
        cpf                        = "123456789",
        endereco                   = "Avenida Z, 30 - Santo Inácio - Bermudas/PI" )

    bruno                          = Cliente(
        nome                       = "Bruno Moura",
        cpf                        = "987654321",
        endereco                   = "Avenida A, 600 - Mato Seco - Ponte Azul/MG" )

    beatriz                        = Cliente(
        nome                       = "Beatriz Souza",
        cpf                        = "123459876",
        endereco                   = "Rua C, 250 - Galho Seco - Ouro Claro/MS" )

    fabio                          = Cliente(
        nome                       = "Fabio Lopes",
        cpf                        = "543219876",
        endereco                   = "Rua Dr. Lopes, 200 - Cabo Verde - Paraisópolis/AM" )

    fabioCC                        = Conta(
        tipo                       = "Conta Corrente",
        agencia                    = "Cabo Verde",
        num                        = 670  ,
        id_cliente                 = 4 ,
        saldo                      = 650.00 )

    fabioCP                        = Conta(
        tipo                       = "Conta Poupança",
        agencia                    = "Cabo Verde",
        num                        = 670  ,
        id_cliente                 = 4 ,
        saldo                      = 10000.00 )

    beatrizCC                      = Conta(
        tipo                       = "Conta Corrente",
        agencia                    = "Galho Seco",
        num                        = 231,
        id_cliente                 = 3 ,
        saldo                      = 7900.00 )

    brunoCP                        = Conta(
        tipo                       = "Conta Poupança",
        agencia                    = "Mato Seco",
        num                        = 134,
        id_cliente                 = 2 ,
        saldo                      = 30000.00 )


    # Enviando para o BD (persistência de dados)
    session.add_all([adriana, bruno, beatriz, fabio])
    session.add_all([brunoCP, beatrizCC, fabioCC, fabioCP])

    session.commit()

print("\n Recuperando Clientes a partir de condição de filtragem \n")

stmt_clientes                          = select(Cliente).where(Cliente.nome.in_( [ "Adriana", "Beatriz", "Fabio"] )  )

for cliente in session.scalars(stmt_clientes):
    print(cliente)

print("\n Recuperando as Contas do Sr. Fabio Lopes (2 --> CC, CP) \n" )

stmt_contas                       = select(Conta).where(Conta.id_cliente.in_([4]))
for conta in session.scalars(stmt_contas):
    print(conta)

print("\n Recuperando Cliente a partir de condição de filtragem em ordem Decrescente \n")

stmt_order                         = select(Cliente).order_by(Cliente.nome.desc())
for result in session.scalars(stmt_order):
    print(result)

print("\n Recuperando Cliente a partir de condição de filtragem de CPF \n")

stmt_order                         = select(Cliente).order_by(Cliente.cpf)
for result in session.scalars(stmt_order):
    print(result)

print("\n Recuperando Cliente a partir de condição de filtragem de join de nome e conta\n")

stmt_join                          = select(Cliente.nome, Conta.id_cliente ).join_from(Conta, Cliente)
for result in session.scalars(stmt_join):
    print(result)

print( select(Cliente.nome, Conta.id_cliente ).join_from(Conta, Cliente) )

connection                         = engine.connect()
results                            = connection.execute(stmt_join).fetchall()

print("\n Executando statement a partir da connection \n")

for result in results:
    print(result)

print("\n Total de instâncias do Cliente \n")
stmt_count                         = select(func.count('*')).select_from(Cliente)
for result in session.scalars(stmt_count):
    print(result)