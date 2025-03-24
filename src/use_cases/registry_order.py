
from datetime import datetime
from src.models.repository.interfaces.orders_repository import OrdersRepositoryInterface
from src.main.http_types.http_request import HttpRequest
from src.main.http_types.http_response import HttpResponse
from src.validators.registry_order_validator import registry_order_validator

class RegistryOrder:
    def __init__(self, orders_repository: OrdersRepositoryInterface) -> None:
        self.__orders_repository = orders_repository

    def registry(self, http_request: HttpRequest ) -> HttpResponse:
        try:
            body = http_request.body
            self.__validate_body(body) # Extração e validação do conteúdo
            
            new_order = self.__format_new_order(body) # Formatação dos dados
            self.__registry_order(new_order) # Registro do novo dado/pedido
                        
            return self.__format_reponse() # Formatação de resposta do dado
        except Exception as exception: # Fazer um teste unitario para esse erro
            return HttpResponse(
                body= { "error": str(exception) }, 
                status_code=400
            )
            
    def __validate_body(self, body: dict) -> None:
        registry_order_validator(body) # Tratamento com o body 
    
    # a logica tem uma operação e o formato da reposta outra
    def __format_new_order(self, body: dict) -> dict:
        new_order = body["data"]
        new_order = {**new_order, "created_at": datetime.now() }
        return new_order 
    
    def __registry_order(self, new_order: dict) -> None:
        self.__orders_repository.insert_document(new_order)
    
    def __format_reponse(self) -> dict:
        return HttpResponse(
            body={
                "data": {
                    "type": "Order",
                    "count": 1,
                    "registry": True
                }   
            },
            status_code=201
        )
        