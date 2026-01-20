from fastapi import APIRouter, Depends
from app.utils.dependencies import get_current_user

router = APIRouter(
    prefix="/security-test",
    tags=["Security Test"]
)

@router.get("/protected")
def protected_route(user=Depends(get_current_user)):
    return {
        "message": "JWT is working",
        "user_email": user.email
    }
