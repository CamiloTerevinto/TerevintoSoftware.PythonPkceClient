class TokenConfigMap():
    """
    Defines how to map the response from the OAuth server to the PkceToken class
    """

    def __init__(self, token_type: str = 'token_type', expires_in: str = 'expires_in', access_token: str = 'access_token',
                     id_token: str = 'id_token', scopes: str = 'scopes', refresh_token: str = 'refresh_token'): 
            """
            Initializes a TokenConfigMap object.
            
            Args:
                token_type (str): The key for the token type field. Defaults to 'token_type'.
                expires_in (str): The key for the expiration time field. Defaults to 'expires_in'.
                access_token (str): The key for the access token field. Defaults to 'access_token'.
                id_token (str): The key for the ID token field. Defaults to 'id_token'.
                scopes (str): The key for the scopes field. Defaults to 'scopes'.
                refresh_token (str): The key for the refresh token field. Defaults to 'refresh_token'.
            """

            self.token_type = token_type
            self.expires_in = expires_in
            self.access_token = access_token
            self.id_token = id_token
            self.scopes = scopes
            self.refresh_token = refresh_token
