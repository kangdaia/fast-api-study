from typing import Annotated, Union
from datetime import datetime, timedelta
from app.auth.users_model import UserCreate, UserUpdate, Token
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from app.repository.mongo_handler import MongonHandler

import bcrypt
import os

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/user/login")


def create_user(db_name, collection_name, user_info: UserCreate):
    db = MongonHandler()
    data = {
        "username": user_info.username,
        "email": user_info.email,
        "hashed_password": bcrypt.hashpw(
            (user_info.password1).encode("utf-8"), bcrypt.gensalt()
        ),
    }
    db.insert_item_one(data, db_name=db_name, collection_name=collection_name)
    db.end_client()


def create_access_token(data, expires_delta: Union[timedelta, None] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, os.environ["SECRET_KEY_SSL"], algorithm=os.environ["ALGORITHM"]
    )
    return encoded_jwt


def get_exist_user(db_name, collection_name, create_user: UserCreate):
    user = get_user(
        db_name, collection_name, username=create_user.username, email=create_user.email
    )
    return user


def get_user(db_name, collection_name, username, email=None):
    db = MongonHandler()
    if username is None:
        return None
    user = db.find_item_one(
        {
            "$or": [
                {"email": username if email is None else email},
                {"username": username},
            ]
        },
        db_name=db_name,
        collection_name=collection_name,
    )
    db.end_client()
    return user


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(
            token, os.environ["SECRET_KEY_SSL"], algorithms=[os.environ["ALGORITHM"]]
        )
        username = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    user = get_user(
        db_name="fast-api-test-dk", collection_name="user", username=username
    )
    if user is None:
        raise credentials_exception
    return user


def authenticate_user(db_name, collection_name, username, password):
    user = get_user(db_name, collection_name, username)
    if not user:
        return False
    if not bcrypt.checkpw(password.encode("utf-8"), user["hashed_password"]):
        return False
    return user


def update_user_info(
    db_name, collection_name, username, update_user: UserUpdate, email=None
):
    db = MongonHandler()
    if username is None or update_user is None:
        return None
    if update_user.password1 is not None:
        update_value = {
            "username": update_user.username,
            "email": update_user.email,
            "hashed_password": bcrypt.hashpw(
                (update_user.password1).encode("utf-8"), bcrypt.gensalt()
            ),
        }
    else:
        update_value = {"username": update_user.username, "email": update_user.email}
    user = db.update_item_one(
        {
            "$or": [
                {"email": username if email is None else email},
                {"username": username},
            ]
        },
        db_name=db_name,
        collection_name=collection_name,
        update_value={"$set": update_value},
    )
    db.end_client()
    return user


def delete_user(db_name, collection_name, username, email=None):
    db = MongonHandler()
    if username is None:
        return None
    result = db.delete_item_one(
        condition={
            "$or": [
                {"email": username if email is None else email},
                {"username": username},
            ]
        },
        db_name=db_name,
        collection_name=collection_name,
    )
    return result
