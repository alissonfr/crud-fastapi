from pydantic import BaseModel

class UserResponse(BaseModel):
    email: str
    password: str
    name: str

