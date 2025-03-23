class HttpRequest:
    def __init__(self, body: dict = None, header: dict = None) -> None:
        self.body = body
        self.headers = header
        