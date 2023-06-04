from pydantic import BaseModel, Field



class RegisterArgument(BaseModel):
    user_id: str 
    user_pw: str 
    user_nm: str 

