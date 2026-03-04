from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer

router = APIRouter(prefix="/documents", tags=["Documents"])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

@router.get("/")
def get_documents(token: str = Depends(oauth2_scheme)):
    return {"message": "You are authenticated", "token": token}