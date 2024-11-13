from fastapi import APIRouter, HTTPException
from services import user_service
from models import UserCreate

router = APIRouter()


@router.get("/users/{user_id}")
async def get_user(user_id: int):
    user = user_service.get_user_by_id(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.post("/user")
async def post_user(user: UserCreate):
    created_user = user_service.create_user(user)
    return {"message": "User created successfully", "user": created_user}
