from db_connection import exec_query
from route import user
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from starlette.middleware.cors import CORSMiddleware
from exception import *
from db_connection import exec_fetch_query, exec_query


app = FastAPI()

app.include_router(user.router, prefix="/login", tags=["유저"])


@app.get("/")
async def root():
    try:
        # 연결이 성공하면 현재 시간을 가져오는 쿼리를 실행합니다.
        result = exec_fetch_query("SELECT * FROM my_table WHERE id = %s", ("가가"))
        print(f"현재 시간은: {result[0]}")
    except Exception as e:
        # 만약 연결이 실패하거나 오류가 발생하면 그 이유를 출력합니다.
        print(f"데이터베이스 연결에 실패했습니다: {str(e)}")


origins = [
    "*"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.exception_handler(LOADITDBRequestFailException)
async def db_request_exception_handler(request: Request, exc: LOADITDBRequestFailException):
    return JSONResponse(status_code=400, content=exc.response_content)