from urllib.parse import urlencode
from webbrowser import open_new
from requests import post

from .login_config import PkceLoginConfig
from .pkce_token import PkceToken
from .internal.oauth_http_server import OAuthHttpServer
from .internal.oauth_http_handler import OAuthHttpHandler
from .internal.helpers import generate_pkce_code_pair, generate_random_alphanumeric_string

class PkceClient():
    def __init__(self, login_config: PkceLoginConfig) -> None:
        if not login_config:
            raise ValueError("A valid LoginConfig instance is required")
        
        self.__login_config = login_config
        self.__token: "PkceToken | None" = None

    def login(self) -> PkceToken:
        with OAuthHttpServer(('', self.__login_config.internal_port), OAuthHttpHandler) as httpd:
            code_verifier, code_challenge = generate_pkce_code_pair()

            redirect_uri = f"http://localhost:{self.__login_config.internal_port}"

            if len(self.__login_config.redirect_uri_extension) > 0:
                redirect_uri = f"{redirect_uri}/{self.__login_config.redirect_uri_extension}"

            login_uri = self.__generate_login_uri(self.__login_config, code_challenge, redirect_uri)

            open_new(login_uri)

            httpd.handle_request()

            auth_code = httpd.authorization_code

            data = {
                "code": auth_code,
                "client_id": self.__login_config.client_id,
                "grant_type": "authorization_code",
                "scopes": self.__login_config.scopes,
                "redirect_uri": redirect_uri,
                "code_verifier": code_verifier
            }

            response = post(self.__login_config.token_uri, data=data, verify=self.__login_config.verify_authorization_server_https)

            jwt_token: dict = response.json()

            self.__token = PkceToken(**jwt_token)

            return self.__token
    
    def get_access_token(self) -> "str | None":
        if not self.__token:
            return None
        
        return self.__token.access_token
    
    def get_id_token(self) -> "str | None":
        if not self.__token:
            return None
        
        return self.__token.id_token
    
    def signin_silent(self) -> PkceToken:
        if not self.__token:
            return self.login()
        
        if not self.__token.refresh_token:
            raise Exception("Silent sign-in is not possible without a refresh token")
        
        data = {
            "client_id": self.__login_config.client_id,
            "grant_type": "refresh_token",
            "refresh_token": self.__token.refresh_token,
            "scopes": self.__login_config.scopes,
        }

        response = post(self.__login_config.token_uri, data=data, verify=self.__login_config.verify_authorization_server_https)

        jwt_token: dict = response.json()

        self.__token = PkceToken(**jwt_token)

        return self.__token

    def __generate_login_uri(self, login_config: PkceLoginConfig, code_challenge: str, redirect_uri: str) -> str:
        params = {
            "client_id": login_config.client_id,
            "response_type": "code",
            "redirect_uri": redirect_uri,
            "code_challenge_method": "S256",
            "code_challenge": code_challenge
        }

        if login_config.scopes and len(login_config.scopes) > 0:
            scope = " ".join(login_config.scopes)
            params["scope"] = scope

        if login_config.add_random_state:
            state = generate_random_alphanumeric_string(
                login_config.random_state_length)
            params["state"] = state

        query = urlencode(params)

        return f"{login_config.authorization_uri}?{query}"