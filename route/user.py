from fastapi import APIRouter, Header, Request, Query, Body
from fastapi.responses import JSONResponse
from auth1.jwt import get_user_id_from_jwt
from controller.user import * 
from model.user import *



router=APIRouter()



@router.get("", summary="유저 정보 조회", description="토큰으로 유저 정보 조회")
def route_get_user(Authorization: str = Header(None)):
    user_id, user_pw = get_user_id_from_jwt(Authorization)

    status_code, result = get_user(user_id, user_pw)

    return JSONResponse(status_code=status_code, content=result)




@router.post("", description="유저 등록")
def route_post_user(user_info: RegisterArgument):
    print(user_info)
    status_code = post_user({**jsonable_encoder(user_info)})

    return JSONResponse(status_code=status_code, content={"status_code": status_code})




@router.post("/login", summary="로그인", description="로그인 및 토큰 발급")
def route_post_login(
        request: Request,
    user_id: str = Body(...),
    user_pw: str = Body(...),
):
    status_code, result = post_user_login(user_id, user_pw)

    return JSONResponse(status_code=status_code, content=result)


