class UsuarioException(Exception):
    ...

class UsuarioNotFoundError(UsuarioException):
    def __init__(self):
        self.status_code = 404
        self.detail = "USUARIO_NAO_ENCONTRADO"


class UsuarioAlreadyExistError(UsuarioException):
    def __init__(self):
        self.status_code = 409
        self.detail = "EMAIL_DUPLICADO"

class SalaException(Exception):
    ...

class SalaNotFoundError(SalaException):
    def __init__(self):
        self.status_code = 404
        self.detail = "SALA_NAO_ENCONTRADA"

class JogoException(Exception):
    ...

class JogoNotFoundError(JogoException):
    def __init__(self):
        self.status_code = 404
        self.detail = "JOGO_NAO_ENCONTRADO"