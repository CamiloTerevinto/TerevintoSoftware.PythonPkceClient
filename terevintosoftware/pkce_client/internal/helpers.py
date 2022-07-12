from random import SystemRandom
from string import ascii_letters, digits
from hashlib import sha256
from base64 import urlsafe_b64encode
from typing import Tuple

def generate_pkce_code_pair() -> Tuple[str, str]:
    code_verifier = generate_random_alphanumeric_string(128)

    code_sha_256 = sha256(code_verifier.encode('utf-8')).digest()
    b64 = urlsafe_b64encode(code_sha_256)
    code_challenge = b64.decode('utf-8').replace('=', '')

    return (code_verifier, code_challenge)


def generate_random_alphanumeric_string(length: int) -> str:
    system_random = SystemRandom()
    return ''.join(system_random.choices(ascii_letters + digits, k=length))
