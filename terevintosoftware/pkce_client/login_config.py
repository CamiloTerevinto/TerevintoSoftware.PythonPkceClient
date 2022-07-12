from typing import List


class PkceLoginConfig():
    def __init__(self, authorization_uri: str, token_uri: str, scopes: List[str], client_id: str, internal_port: int, 
        add_random_state: bool, random_state_length: int = 0, verify_authorization_server_https: bool = True) -> None:
        if not authorization_uri or authorization_uri == "":
            raise ValueError("An authorization_uri is required")

        if not token_uri or token_uri == "":
            raise ValueError("A token_uri is required")

        if not scopes or len(scopes) < 1:
            scopes = []

        if not client_id or client_id == "":
            raise ValueError("A client_id is required")

        if not internal_port or internal_port < 1 or internal_port > 65535:
            raise ValueError("A valid port is required, normally between 1024 and 65535, such as 8080")
        
        self.authorization_uri = authorization_uri
        self.token_uri = token_uri
        self.scopes = scopes
        self.client_id = client_id
        self.internal_port = internal_port
        self.verify_authorization_server_https = verify_authorization_server_https
        self.add_random_state = add_random_state
        self.random_state_length = random_state_length