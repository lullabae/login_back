from db_connection import exec_fetch_query
from exception import *
import jwt
from fastapi import Header
from query import user as query
import json

secret_key = "rjsanfwn"
algorithm = ["HS256"]

# JWT로부터 LOADIT 'USER_ID'와 'ADMIN_USER_ID' 얻기
def get_user_id_from_jwt(token_header: str) -> str:
    print(token_header)
    try:
        if not token_header:
            raise AuthHeaderNotIncludedException

        token = token_header[7:]
        decoded_token = jwt.decode(token, secret_key, algorithms=algorithm)

        return decoded_token.get("identity")

    except (IndexError, jwt.PyJWTError):
        raise InvalidUserIdException



