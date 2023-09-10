from fastapi import APIRouter

router = APIRouter()

@router.post('/login')
def login():
    return []

@router.delete('/logout')
def logout():
    return []