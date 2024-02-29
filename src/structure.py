import pydantic
from enum import Enum


class Group(str, Enum):
    user = 'user'
    premium = 'premium'
    admin = 'admin'


class User(pydantic.BaseModel):
    firstName: str
    lastName: str
    birthYear: int
    group: Group
