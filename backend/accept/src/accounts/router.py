from fastapi import APIRouter

router = APIRouter()

@router.get("/user")
async def info_user():
    return(
)