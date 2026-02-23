from fastapi import APIRouter, HTTPException
from schema import User, UserCreate
import json
import os

router = APIRouter()

FILE_PATH = "users.txt"


# -------- Helper Functions -------- #

def read_users():
    if not os.path.exists(FILE_PATH):
        return []
    with open(FILE_PATH, "r") as file:
        try:
            return json.load(file)
        except:
            return []


def write_users(users):
    with open(FILE_PATH, "w") as file:
        json.dump(users, file, indent=4)


def get_next_id(users):
    if not users:
        return 1
    return max(user["id"] for user in users) + 1


# -------- Routes -------- #

@router.post("/")
def create_user(user: UserCreate):
    users = read_users()
    new_user = user.dict()
    new_user["id"] = get_next_id(users)

    users.append(new_user)
    write_users(users)

    return new_user


@router.get("/")
def get_all_users():
    return read_users()


# IMPORTANT: search must come BEFORE /{id}
@router.get("/search")
def search_users(q: str):
    users = read_users()
    results = [u for u in users if q.lower() in u["name"].lower()]
    return results


@router.get("/{id}")
def get_user(id: int):
    users = read_users()
    for user in users:
        if user["id"] == id:
            return user
    raise HTTPException(status_code=404, detail="User not found")


@router.put("/{id}")
def update_user(id: int, updated: UserCreate):
    users = read_users()
    for user in users:
        if user["id"] == id:
            user["name"] = updated.name
            user["email"] = updated.email
            write_users(users)
            return user

    raise HTTPException(status_code=404, detail="User not found")


@router.delete("/{id}")
def delete_user(id: int):
    users = read_users()
    for user in users:
        if user["id"] == id:
            users.remove(user)
            write_users(users)
            return {"message": "User deleted"}

    raise HTTPException(status_code=404, detail="User not found")