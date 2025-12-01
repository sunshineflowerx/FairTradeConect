import json 
from abc import ABC, abstractmethod
from typing import Dict, Any, Union
import datetime

# definição de tipos:
Request = Dict[str, Any]
Response = Union[Dict[str, Any], str]

# 1. Interface (receber os dados)
class HttpHandler(ABC):
    """_summary-
    - Define uma interface comum: Entre requisição e os Middlewares.
    Args:
        ABC (_type_): _description_
    """
    @abstractmethod
    def handle(self, request: Request) -> Response:
        pass


# 2. Componentes Concretos (Regras de Negócio)
class UserProfileHandler(HttpHandler):
    """Processa a logica de neócio e devolve os dados do usuário.
    """
    def handle(self, request: Request) -> Response:
        print("-> [Núcleo] Consultando banco de dados...")
        # extrai o ID da final da URL
        user_id = request.get("path", "").split("/")[-1]
        
        #retorno Dicionário:
        return {
            "status": 200,
            "data": {
                "id": user_id,
                "name": "Maria Silva",
                "role": "Backend Student",
                "active": True
            }
        }

# 3. Decorator Base (Middleware)
class Middleware(HttpHandler):
    """Classe base que implementa o padrão do decorator"""
    def __init__(self, next_handler: HttpHandler):
        self._next_handler = next_handler
        
    def handle(self, request: Request) -> Response:
        return self._next_handler.handle(request)


# 4. Decorators Concretos (Handler 1: Handler 2: Auth, Handler 3: Json, Handler 4: Log)
class AuthMiddleware(Middleware):
    """Padrão Proxy/Decorator: Aplicar um logica antes"""
    def handle(self, request: Request) -> Response:
        print("[Auth] Verificando credenciais do Usuário")
        
        handers = request.get("headers", {})
        token = handers.get("Authorization", "")
        if token != "SENHA_SECRETA":
            print("[Auth] Token inválido ou ausente")
            return {"status": 403, "erro": "Invalid Token"}
        
        print("[Auth] Token Válido")
        # Se o token é válido, passo para o próximo handler
        return super().handle(request)

class LoggingMiddleware(Middleware):
    def handle(self, request: Request) -> Response:
        #antes da execução do handler
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        path = request.get("path", "/")
        print(f"[LOG {timestamp}] - Requisição iniciada para: {path}")
        
        response = super().handle(request)
        
        #depois da execução do handler
        status = "OK"
        if isinstance(response, dict):
            status = response.get('status')
        
        print(f"[LOG] {timestamp} - Requisição finalizada. Status {status}")
        return response

class JSONResponseMiddleware(Middleware):
    def handle(self, request: Request) -> Response:
        raw_response = super().handle(request)
        # transformação: Dict -> JSON (pós-processamento)
        if isinstance(raw_response, dict):
            print("Serializando Dict para JSON")
            return json.dumps(raw_response, indent=4)
        return raw_response

if __name__ == "__main__":
    core_handler = UserProfileHandler()
    # JSON -> LOG -> Auth -> Core -> (volta) -> Auth -> Log -> JSON
    application = JSONResponseMiddleware(
        LoggingMiddleware(
            AuthMiddleware(
                core_handler
            )
        )
    )
    
    print("Servidor Pronto.")
    
    # Simulação: token valido
    request_admin = {
        "path": "/api/users/10",
        "headers": {
            "Authorization": "SENHA_SECRETA",
            "User-Agent": "Postman"
        }
    }
    
    response = application.handle(request_admin)
    print(f"RESPOSTA HTTP: \n {response}")