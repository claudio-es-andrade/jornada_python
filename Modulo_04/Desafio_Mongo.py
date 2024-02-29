import pymongo
import pymongo as pyM
import pprint

client = pyM.MongoClient("mongodb+srv://<nome>:<senha>@cluster2000.f2mi0nm.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client.test
collection = db.test_collection

post = [
    {
        "nome": "Adriana Ramos",
        "cpf": "123456789",
        "endereco": "Avenida Z, 30 - Santo Inácio - Bermudas/PI"
    },
    {
        "nome": "Bruno Moura",
        "cpf": "987654321",
        "endereco": "Avenida A, 600 - Mato Seco - Ponte Azul/MG",
        "contas": [
            {
                "tipo": "Conta Poupança",
                "agencia": "Mato Seco",
                "num": 134,
                "id_cliente": 2,
                "saldo": 30000.00
            }
        ]
    },
    {
        "nome": "Beatriz Souza",
        "cpf": "123459876",
        "endereco": "Rua C, 250 - Galho Seco - Ouro Claro/MS",
        "contas": [
            {
                "tipo": "Conta Corrente",
                "agencia": "Galho Seco",
                "num": 231,
                "id_cliente": 3,
                "saldo": 7900.00
            }
        ]
    },
    {
        "nome": "Fabio Lopes",
        "cpf": "543219876",
        "endereco": "Rua Dr. Lopes, 200 - Cabo Verde - Paraisópolis/AM",
        "contas": [
            {
                "tipo": "Conta Corrente",
                "agencia": "Cabo Verde",
                "num": 670,
                "id_cliente": 4,
                "saldo": 650.00
            },
            {
                "tipo": "Conta Poupança",
                "agencia": "Cabo Verde",
                "num": 670,
                "id_cliente": 4,
                "saldo": 10000.00
            }
        ]
    }
]

posts = db.posts
post_ids = posts.insert_many(post)
print(post_ids.inserted_ids)

print(db.list_collection_names())
print(posts.find_one())
pprint.pprint(posts.find_one())

# playing with more Statements:

print("\n Printing more Statements...")

print("\n Documentos presentes na coleção posts")
for post in posts.find():
    pprint.pprint(post)
print(posts.count_documents({}))
print(posts.count_documents({"nome": "Bruno Moura"}))
print(posts.count_documents({"tags": "insert"}))

pprint.pprint(posts.find_one({"tags": "insert"}))
print("\n Recuperando info da coleção Post de maneira ordenada")
for post in posts.find({}).sort("num"):
    pprint.pprint(post)

print("\n Resultado da lista da tabela em ordem ascendente")
result                             = db.profiles.create_index([('nome', pymongo.ASCENDING)], unique=True)

print("\n Resultado da Informação do Index")
print(sorted(list(db.profiles.index_information() )))


print("\n Coleções armazenadas no mongoDB")
collections                        = db.list_collection_names()
for collection in collections:
    print(collection)
#db.profiles.drop()

for post in posts.find():
    pprint.pprint((post))

print(posts.delete_one({"nome": "Beatriz Souza"}))




#bulk inserts
new_posts                          = [{

        "contas": [
            {
                "tipo": "Conta Corrente",
                "agencia": "Santo Inácio",
                "num": 125,
                "id_cliente": 1,
                "saldo": 60000.00
            },
            {
                "tipo": "Conta Poupança",
                "agencia": "Santo Inácio",
                "num": 125,
                "id_cliente": 1,
                "saldo": 200000.00
            }
        ]

                                   }]

result = db.posts.insert_many(new_posts)
print(result.inserted_ids)

print("\nRecuperação Final:")
adriana_ramos_accounts = db.posts.find_one({"nome": "Adriana Ramos"})
pprint.pprint(adriana_ramos_accounts)

print("\nDocumentos presentes na coleção posts:")
for post in db.posts.find():
    pprint.pprint(post)

print(posts.drop())
