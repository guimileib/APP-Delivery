from src.main.http_types.http_request import HttpRequest
from .registry_order import RegistryOrder

class OrdersRepositoryMock:
    def __init__(self) -> None:
        self.insert_document_att = {}
        
    def insert_document(self, document: dict) -> None:
        self.insert_document_att["document"] = document
        
class OrdersRepositoryMockError:
    def insert_document(self, document: dict) -> None:
        raise Exception("erro aqui")

def test_registry():
    repo = OrdersRepositoryMock()
    registry_order = RegistryOrder(repo)
    
    mock_registry = HttpRequest(
        body= {
            "data": {
                "name": "joaozinho",
                "address": "rua do limao",
                "cupom": False,
                "items": [
                    {"item": "Refrigerante", "quantidade": 2},
                    {"item": "pizza", "quantidade": 3}
                ]
            }
        }
    )   
    
    reponse = registry_order.registry(mock_registry)
    
    assert "name" in repo.insert_document_att["document"]
    assert "address" in repo.insert_document_att["document"]
         