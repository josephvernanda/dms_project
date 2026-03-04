from fastapi import APIRouter

router = APIRouter(prefix="/permissions", tags=["Documents"])

@router.get("/")
def test_documents():
    return {"message": "Permissions route working"}