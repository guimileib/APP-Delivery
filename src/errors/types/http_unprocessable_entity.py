# Requisição recebeu uma entidade, mas não é conhecida -> body esta formatado de uma forma que não é conhecida
class HttpUnprocessableEntityError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message
        self.name = "UnprocessableEntity"
        self.status_code = 422
        