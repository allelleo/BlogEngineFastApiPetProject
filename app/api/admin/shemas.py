import pydantic

class LoginShema(pydantic.BaseModel):
    username: str
    password: str