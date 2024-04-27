from jwt import encode, decode

def create_token(data: dict):
    token: str = encode(payload=data, key="my_secret_key", algorithm="HS256") # Payload es la data que se va a encriptar, key es la clave para encriptar y algorithm es el algoritmo de encriptacion, en este caso HS256 que es el que se suele usar
    return token

def validate_token(token: str) -> dict:
    data: dict = decode(token, key="my_secret_key", algorithms=["HS256"]) # Los parámetros de "decode" son el token a desencriptar, la clave para desencriptar y el algoritmo de desencriptación, en este caso el algoritmo de desecriptación se envía como lista ya que puede ser más de uno y es lo correcto hacerlo así
    return data