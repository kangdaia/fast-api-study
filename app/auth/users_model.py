from pydantic import BaseModel, EmailStr, validator
import re
from app.musics.musics_model import Music
from typing import Union


class Token(BaseModel):
    access_token: str
    token_type: str


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password1: str
    password2: str

    @validator("username", "password1", "password2", "email")
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError("빈 값은 허용되지 않습니다.")
        return v

    @validator("password2")
    def passwords_match(cls, v, values):
        if "password1" in values and v != values["password1"]:
            raise ValueError("비밀번호가 일치하지 않습니다")
        return v

    @validator("password1")
    def password_pattern(cls, v):
        # 대문자, 소문자, 숫자, 기호 최소 1개이상 포함, 8자 이상 비밀번호
        password_format = (
            r"(?=.*[\d])(?=.*[A-Z])(?=.*[a-z])(?=.*[!@#$%^&+=?.])[\w\d!@#$%^&+=.]{8,}"
        )
        if not re.fullmatch(password_format, v):
            raise ValueError("비밀번호가 규칙에 맞지 않습니다")
        return v


class User(BaseModel):
    username: str
    email: EmailStr
    hashed_password: str


class UserUpdate(UserCreate):
    old_password: str

    # override UserCreate validator for non empty value. UserUpdate Can be empty.
    @validator("username", "password1", "password2", "email")
    def not_empty_allow(cls, v):
        return v
