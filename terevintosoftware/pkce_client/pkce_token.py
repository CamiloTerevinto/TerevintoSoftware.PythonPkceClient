class PkceToken():
    def __init__(self, token_type: str, expires_in: int, scope: str, 
            access_token: "str | None" = None, id_token: "str | None" = None, 
            refresh_token: "str | None" = None) -> None:
            
        self.token_type = token_type
        self.expires_in = expires_in
        self.access_token: "str | None" = access_token
        self.id_token: "str | None" = id_token
        self.scopes = scope.split(" ") if scope else []
        self.refresh_token: "str | None" = refresh_token
