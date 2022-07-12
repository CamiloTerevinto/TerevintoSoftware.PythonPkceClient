# Python PKCE Client

This python package contains a simple client to request tokens using the OAuth 2/OIDC Authorization Code PKCE flow.

## Sample usage

```python
from terevintosoftware.pkce_client import PkceClient, PkceLoginConfig

config = PkceLoginConfig(
    authorization_uri="https://localhost:44300/connect/authorize",
    token_uri="https://localhost:44300/connect/token",
    scopes=[ "openid", "profile", "api" ],
    client_id="python-nb",
    internal_port=8888,
    add_random_state=True,
    random_state_length=32,
    verify_authorization_server_https=False
)

login_client = PkceClient(config)
pkce_token = login_client.login()
headers = { "Authorization": "Bearer " + str(pkce_token.access_token) }
```
