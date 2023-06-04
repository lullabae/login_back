from db_connection import exec_fetch_query, exec_query
from starlette.status import *
from fastapi.encoders import jsonable_encoder
from query import user as query
from datetime import datetime, timedelta
from exception import LOADITDBRequestFailException
from mysql.connector import errors
from model.user import *

import jwt
import json


def get_user_info():
    print(1)
    result = exec_fetch_query(query.SELECT_USER_INFO + ";",)
    if not result:
        return HTTP_404_NOT_FOUND, {"message": "회원 정보를 찾을 수 없습니다.", "result": {}}
    print(result)
    result = {
        **jsonable_encoder(result[0])
    }

    return HTTP_200_OK, {"message": "OK", "result": result}


def get_user(user_id:str, user_pw:str):
    """
    유저 정보 조회
    """
    result = exec_fetch_query(query.SELECT_USER + ";", {"user_id": user_id, "user_pw": user_pw})

    if not result:
        return HTTP_404_NOT_FOUND, {"message": "회원 정보를 찾을 수 없습니다.", "result": {}}

    result = {
        **jsonable_encoder(result[0])
    }

    return HTTP_200_OK, {"message": "OK", "result": result}



# 회원가입
def post_user(user_info: RegisterArgument):
    print(1,user_info)
    try:
        exec_query(query.INSERT_USER, user_info)

    except errors.Error as e:
        raise LOADITDBRequestFailException(e)

    return HTTP_200_OK    



# 로그인
def post_user_login(user_id: str, user_pw: str):
    """
    로그인
    """

    query_result = exec_fetch_query(
        query.SELECT_USER_LOGIN_ID_PW,
        {
            "user_id": user_id,
            "user_pw": user_pw,
        },
    )

    if not query_result:
        return HTTP_403_FORBIDDEN, {
            "code": "FAILED",
            "message": "FAILED",
        }

    query_result = jsonable_encoder(query_result)

    # JWT 발행 시각
    issued_timestamp = datetime.utcnow()

    # JWT 만료 시각
    expiration_timestamp = datetime.utcnow() + timedelta(days=1)

    token = jwt.encode(
        {
            "identity": [query_result[0].get("USER_ID"), query_result[0].get("USER_PW")],
            "iat": issued_timestamp,
            "exp": expiration_timestamp,
            "type": "access",
        },
        "rjsanfwn",
    )
    
    return HTTP_200_OK, {"code": "OK", "message": "OK", "token": f"Bearer {token}" }






