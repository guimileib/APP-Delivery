from bson.objectid import ObjectId

class OrdersRepository:
    def __init__(self, db_connection) -> None:
        self.__collection_name = 'orders' # collection name in MongoDB
        self.__db_connetion = db_connection
        
    def insert_document(self, document: dict) -> None:
        collection = self.__db_connetion.get_collection(self.__collection_name) # get_collection is a method from pymongo
        collection.insert_one(document)
    
    def insert_list_of_documents(self, list_of_documents: list) -> None:
        collection = self.__db_connetion.get_collection(self.__collection_name)
        collection.insert_many(list_of_documents)
    
    def select_many(self, doc_filter: dict) -> list:
        collection = self.__db_connetion.get_collection(self.__collection_name)
        data = collection.find(doc_filter)
        return data        
    
    def select_one(self, doc_filter: dict) -> list:
        collection = self.__db_connetion.get_collection(self.__collection_name)
        response = collection.find_one(doc_filter)
        return response
    
    def select_many_with_properties(self, doc_filter: dict) -> list:
        collection = self.__db_connetion.get_collection(self.__collection_name)
        data = collection.find(
            doc_filter, # filtro de busca
            {"_id": 0, "cupom": 0 } # opções de retorno
        )
        return data
    
    def select_if_property_exists(self) -> dict:
        collection = self.__db_connetion.get_collection(self.__collection_name)
        response = collection.find_one(
            {"address": {"$exists": True}},
            {"_id": 0, "cupom": 0 }) # verifica se existe essa propriedade nos documentos do nosso banco
        return response
    
    def select_by_object_dict(self, object_id: str) -> dict:
        collection = self.__db_connetion.get_collection(self.__collection_name)
        data = collection.find_one({"_id": ObjectId(object_id)}) # utilizo o 'find_one' para pela unicidade do objectid
        return data
    