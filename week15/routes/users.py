from fastapi import APIRouter, HTTPException
from schema import UserCreate
from user_store import UserStore

router = APIRouter()
store = UserStore("users.db")  # now uses SQLite database

# -------- Routes -------- #

@router.post("/")
def create_user(user: UserCreate):
    new_user = store.save(user.dict())
    return new_user

@router.get("/")
def get_all_users():
    return store.load()

@router.get("/search")
def search_users(q: str):
    users = store.load()
    results = [u for u in users if q.lower() in u["name"].lower()]
    return results

@router.get("/{id}")
def get_user(id: int):
    user = store.find_by_id(id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/{id}")
def update_user(id: int, updated: UserCreate):
    success = store.update_user(id, updated.dict())
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User updated"}

@router.delete("/{id}")
def delete_user(id: int):
    success = store.delete_user(id)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted"}