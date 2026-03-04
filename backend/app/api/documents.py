from fastapi import APIRouter, Depends
from app.core.deps import get_current_user

router = APIRouter(prefix="/documents", tags=["Documents"])

@router.get("/")
def get_documents(current_user: str = Depends(get_current_user)):
    return {
        "message": "Access granted",
        "user": current_user
    }