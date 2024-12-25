from pydantic import BaseModel

# Схема для создания пользователя
class CreateUser(BaseModel):
    username: str
    firstname: str
    lastname: str
    age: int

# Схема для обновления пользователя
class UpdateUser(BaseModel):
    firstname: str
    lastname: str
    age: int
