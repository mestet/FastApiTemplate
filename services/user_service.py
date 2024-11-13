from repositories.user_repository import fetch_user_by_id, insert_user
from models import UserCreate


def get_user_by_id(user_id: int):
    return fetch_user_by_id(user_id)


def create_user(user: UserCreate):
    return insert_user(user)
