from fastapi import APIRouter

router = APIRouter(prefix="/notifications", tags=["Documents"])

@router.get("/")
def test_documents():
    return {"message": "Notifications route working"}