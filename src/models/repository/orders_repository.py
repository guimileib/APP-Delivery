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
    # Update
    def edit_registry(self) -> None:
        collection = self.__db_connetion.get_collection(self.__collection_name)    
        collection.update_one(
            { "_id": ObjectId("67c9d88c88664a49cfa11e7d")}, # filtros - busca
            { "$set": { "itens.pizza.quantidade": 30}} # edição    
            #{ "$set": { "cupom": True}} # edição 
        )
    
    
    def edit_many_registries(self) -> None:
        collection = self.__db_connetion.get_collection(self.__collection_name)    
        collection.update_many(
            { "itens.refrigerante": { "$exists": True } }, # filtros - busca
            { "$set": { "itens.refrigerante.quantidade": 100}} # edição    
            #{ "$set": { "cupom": True}} # edição 
        )
    
    def edit_registry_with_increment(self) -> None:
        collection = self.__db_connetion.get_collection(self.__collection_name)    
        collection.update_one(
            { "_id": ObjectId("67c9d88c88664a49cfa11e7d")}, # filtros - busca
            { "$inc": { "itens.pizza.quantidade": 50}} # vai incrementar 50 na quantidade de pizza  
        )
        
    def edit_registry_with_decrement(self) -> None:
        collection = self.__db_connetion.get_collection(self.__collection_name)
        collection.update_one(
            { "_id": ObjectId("67c9d88c88664a49cfa11e7d")}, # filtros - busca
            { "$inc": { "itens.pizza.quantidade": -50}} # vai decrementar 50 na quantidade de pizza  
        )
    
    def delete_registry(self) -> None:
        collection = self.__db_connetion.get_collection(self.__collection_name)
        collection.delete_one({ "_id": ObjectId('67c9d88c88664a49cfa11e7d')}) # apenas mostrar quem você quer deletar
    
    def delete_many_registries(self) -> None:
        collection = self.__db_connetion.get_collection(self.__collection_name)
        collection.delete_many({ "itens.refrigerante": { "$exists": True } }) # vou deletar aqueles que tem refrigerante como item