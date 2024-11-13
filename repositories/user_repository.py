from database import get_cursor
from models import UserCreate


def fetch_user_by_id(user_id: int):
    with get_cursor() as cur:
        cur.execute("SELECT * FROM users.users WHERE id = %s", (user_id,))
        user = cur.fetchone()
        return user


def insert_user(user: UserCreate):
    with get_cursor() as cur:
        cur.execute("INSERT INTO users (name, email) VALUES (%s, %s) RETURNING id", (user.name, user.email))
        user_id = cur.fetchone()
        return user_id
