from fastapi import APIRouter, HTTPException, Form
from app.core.security import hash_password, verify_password, create_access_token

router = APIRouter(prefix="/auth", tags=["Auth"])

fake_users_db = {}

@router.post("/register")
def register(username: str, password: str):

    if username in fake_users_db:
        raise HTTPException(status_code=400, detail="User already exists")

    fake_users_db[username] = hash_password(password)

    return {"message": "User registered successfully"}


from fastapi import Form

@router.post("/login")
def login(
    username: str = Form(..., description="Enter your username"),
    password: str = Form(..., description="Enter your password")
):
    user = fake_users_db.get(username)

    if not user:
        raise HTTPException(status_code=400, detail="Invalid credentials")

    if not verify_password(password, user):
        raise HTTPException(status_code=400, detail="Invalid credentials")

    access_token = create_access_token({"sub": username})

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }