from src.main.http_types.http_response import HttpResponse
from src.errors.types.http_not_found import HttpNotFoundError
from src.errors.types.http_unprocessable_entity import HttpUnprocessableEntityError

def error_handler(error: Exception) -> HttpResponse:
    if isinstance(error, (HttpNotFoundError, HttpUnprocessableEntityError)):
        # enviar para um logger
        return HttpResponse(
            status_code=error.status_code,
            body={
                "errors": [{
                    "title": error.name,
                    "detail": error.message
                }]
            }
        )
    # Caso não tenha nenhum erro que se enquadre no de cima
    return HttpResponse(
        status_code=500,
        body={
            "errors": [{
                "title": "Server Error", 
                "detail": str(error)
            }]
        }
    )
