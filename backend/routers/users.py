from fastapi import APIRouter

router = APIRouter()

@router.get('/{user_id}')
def read_user(user_id: str):
    return []

@router.post('/register')
def register_new_user():
    return []

@router.put('/information')
def update_password(password: str):
    return password