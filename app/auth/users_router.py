from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from app.auth import users_crud
from app.auth.users_model import UserCreate, Token, UserUpdate, User
from typing import Annotated
from datetime import timedelta
import os

"""
/user -> get/post/put/delete user query endpoint
"""

router = APIRouter()


# 유저 로그인: access token 부여 방식
@router.post(
    "/login", tags=["user"], description="login for access token", response_model=Token
)
async def login_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
):
    user = users_crud.authenticate_user(
        "fast-api-test-dk", "user", form_data.username, form_data.password
    )
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(
        minutes=int(os.environ["ACCESS_TOKEN_EXPIRE_MINUTES"])
    )
    access_token = users_crud.create_access_token(
        data={"sub": user["username"]}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


# 유저 회원가입
@router.post(
    "/signup",
    tags=["user"],
    description="sign up",
    status_code=status.HTTP_204_NO_CONTENT,
)
def signup_user(user_create: UserCreate):
    user = users_crud.get_exist_user("fast-api-test-dk", "user", user_create)
    if user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="이미 존재하는 사용자입니다."
        )
    users_crud.create_user("fast-api-test-dk", "user", user_create)


# 유저 정보 가져오기
@router.get(
    "/profile",
    tags=["user"],
    description="get user info",
    status_code=status.HTTP_200_OK,
)
def get_user_profile(current_user: User = Depends(users_crud.get_current_user)):
    return {"username": current_user["username"], "email": current_user["email"]}


# 유저 정보 변경
@router.put(
    "/update",
    tags=["user"],
    description="user info update",
    status_code=status.HTTP_204_NO_CONTENT,
)
def change_user_info(
    update_user: UserUpdate, current_user: User = Depends(users_crud.get_current_user)
):
    user = users_crud.authenticate_user(
        "fast-api-test-dk", "user", current_user["username"], update_user.old_password
    )
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="incorrect password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    users_crud.update_user_info(
        "fast-api-test-dk", "user", current_user["username"], update_user
    )


# 유저 탈퇴
@router.delete(
    "/terminate",
    tags=["user"],
    description="terminate account",
    status_code=status.HTTP_204_NO_CONTENT,
)
def terminate_user(password, current_user: User = Depends(users_crud.get_current_user)):
    user = users_crud.authenticate_user(
        "fast-api-test-dk", "user", current_user["username"], password
    )
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="incorrect password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    users_crud.delete_user("fast-api-test-dk", "user", current_user["username"])
