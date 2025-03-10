import pytest
from pymongo import MongoClient
from .orders_repository import OrdersRepository

# não consegui fazer o mock do banco de dados, então criei uma classe para fazer a conexão com o banco de dados
class DBConnectionHandler:
    def __init__(self) -> None:
        self.__connection_string = 'mongodb://{}:{}@{}:{}/?authSource=admin'.format(
            "meuAdmin", # user
            "minhaSenhaForte", # password
            "localhost", # host
            "27017" # porta
        )
        self.__database_name = 'rocket_db'
        self.__client = None
        self.__db_connection = None
        
    def connect_to_db(self):
        self.__client = MongoClient(self.__connection_string)
        self.__db_connection = self.__client[self.__database_name]
        
    def get_db_connection(self):
        return self.__db_connection     

db_connection_handler = DBConnectionHandler()
db_connection_handler.connect_to_db()
conn = db_connection_handler.get_db_connection()

# insere um documento
@pytest.mark.skip(reason="interação com o banco")
def test_insert_document():
    orders_repository = OrdersRepository(conn)
    my_doc = {"alguma": "coisa", "valor": 5} 
    orders_repository.insert_document(my_doc)
    
# insere uma lista de documentos
@pytest.mark.skip(reason="interação com o banco")    
def test_insert_list_of_documents():
    orders_repository = OrdersRepository(conn)
    my_doc = [{"elem1": "coisa"}, {"elem2": "outra coisa"}, {"elem3": "outra coisa"}] 
    orders_repository.insert_list_of_documents(my_doc)
    
# busca com filtro
@pytest.mark.skip(reason="interação com o banco")  
def test_select_many():
    orders_repository = OrdersRepository(conn)
    doc_filter = {"cumpom": True}
    response = orders_repository.select_many(doc_filter)
    print()
    print(response)
    # for nas responsta e printa o doc do banco de dados  
    for doc in response: 
        print(doc)

# busca um documento com filtro
@pytest.mark.skip(reason="interação com o banco")         
def test_select_one():
    orders_repository = OrdersRepository(conn)
    doc_filter = {"cumpom": True}
    response = orders_repository.select_one(doc_filter)
    print()
    print(response)

# busca com filtro e propriedades   
@pytest.mark.skip(reason="interação com o banco")   
def test_select_many_width_properties():
    orders_repository = OrdersRepository(conn)
    doc_filter = {"cupom": True}
    response = orders_repository.select_many_with_properties(doc_filter)
    print()
    for doc in response: 
        print(doc)
        print()
        
# busca para ver se essa propriedade existe
@pytest.mark.skip(reason="interação com o banco")       
def test_select_if_property_exists():
    orders_repository = OrdersRepository(conn)
    response = orders_repository.select_if_property_exists()
    print()
    print(response)
    for doc in response: 
        print(doc)
        print()

# busca com filtro e propriedades   
@pytest.mark.skip(reason="interação com o banco")      
def test_select_many_with_multiple_filter():
    orders_repository = OrdersRepository(conn)
    doc_filter = {
        "cupom": True, # propriedade 
        "itens.doce": {"$exists": True}# propriedade de itens 
        } # Semelhante a uma busca AND em SQL
    
    response = orders_repository.select_many(doc_filter)
    print()
    for doc in response: 
        print(doc)       
        #print(doc["itens"]) 
        print()

# busca com filtro e propriedades   
@pytest.mark.skip(reason="interação com o banco")        
def test_select_many_with_or_filter():
    orders_repository = OrdersRepository(conn)
    doc_filter = { # filtro de busca 
        "$or": [{"address": { "$exists": True}}, # opção de retorno
                {"itens.doce.tipo": "chocolate"}
            ]
    }# Semelhante a uma busca OR em SQL
    
    response = orders_repository.select_many(doc_filter)
    print()
    for doc in response: 
        print(doc)       
        print()

# busca pelo object_id 
def test_select_by_object_dict():
    orders_repository = OrdersRepository(conn)
    # não tenho filtro pois so irei buscar pelo object_id
    object_id = "67c9fe807024a518ba713d2b"
    response = orders_repository.select_by_object_dict(object_id)
    print()
    print(response)
    