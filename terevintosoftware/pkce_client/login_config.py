from typing import List


class PkceLoginConfig():
    def __init__(self, authorization_uri: str, token_uri: str, scopes: List[str], client_id: str, internal_port: int, 
        add_random_state: bool, random_state_length: int = 0, verify_authorization_server_https: bool = True,
        redirect_uri_extension: str = "") -> None:
        """Initializes the configuration for PKCE sign in.

        Args:
            authorization_uri (str): The URL for the OAuth2 Authorization endpoint.
            token_uri (str): The URL for the OAuth2 Token endpoint.
            scopes (List[str]): The list of scopes to request.
            client_id (str): The ID of the client to use.
            internal_port (int): The TCP port to listen for responses from the server.
            add_random_state (bool): Whether to add a random state to the Code request.
            random_state_length (int, optional): The length of the random state created when enabled. Defaults to 0.
            verify_authorization_server_https (bool, optional): Whether to verify the HTTPs connection to the server. Defaults to True.
            redirect_uri_extension (str, optional): An optional suffix to add to the redirect URI, such as /callback. Defaults to "".

        Raises:
            ValueError: The authorization_uri is None or empty.
            ValueError: The token_uri is None or empty.
            ValueError: The client_id is None or empty.
            ValueError: The internal_port is not a valid port number.
            ValueError: The redirect_uri is an absolute uri.
        """

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
        
        if redirect_uri_extension and redirect_uri_extension.startswith("http"):
            raise ValueError("The redirect_uri must be a relative uri (such as /callback for http://localhost/callback)")

        if not redirect_uri_extension:
            redirect_uri_extension = ""
        elif redirect_uri_extension.startswith("/"):
            redirect_uri_extension = redirect_uri_extension.removeprefix("/")
        
        self.authorization_uri = authorization_uri
        self.token_uri = token_uri
        self.scopes = scopes
        self.client_id = client_id
        self.internal_port = internal_port
        self.verify_authorization_server_https = verify_authorization_server_https
        self.add_random_state = add_random_state
        self.random_state_length = random_state_length
        self.redirect_uri_extension = redirect_uri_extension