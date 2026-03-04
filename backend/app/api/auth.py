from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from app.core.security import hash_password, verify_password, create_access_token

router = APIRouter(prefix="/auth", tags=["Auth"])

fake_users_db = {}

# REGISTER
@router.post("/register")
def register(username: str, password: str):

    if username in fake_users_db:
        raise HTTPException(status_code=400, detail="User already exists")

    fake_users_db[username] = hash_password(password)

    return {"message": "User registered successfully"}


# LOGIN (OAuth2 compatible)
@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):

    user = fake_users_db.get(form_data.username)

    if not user:
        raise HTTPException(status_code=400, detail="Invalid credentials")

    if not verify_password(form_data.password, user):
        raise HTTPException(status_code=400, detail="Invalid credentials")

    access_token = create_access_token({"sub": form_data.username})

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }