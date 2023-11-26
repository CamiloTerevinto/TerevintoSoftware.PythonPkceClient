from typing import Any, Dict, List, Union
from .token_config_map import TokenConfigMap

class PkceToken():
    token_type: str
    expires_in: str
    access_token: Union[str, None]
    id_token: Union[str, None]
    scopes: List[str]
    refresh_token: Union[str, None]
    response: Dict[str, Any]

    def __init__(self, token: Dict[str, Any], map: TokenConfigMap):
        self.token_type = token[map.token_type] if map.token_type in token else 'Bearer'
        self.expires_in = token[map.expires_in]
        self.access_token = token[map.access_token] if map.access_token in token else None
        self.id_token = token[map.id_token] if map.id_token in token else None
        self.scopes = token[map.scopes].split(' ') if isinstance(token[map.scopes], str) \
            else token[map.scopes]
        self.refresh_token = token[map.refresh_token] if map.refresh_token in token else None
        self.response = token

