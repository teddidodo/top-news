from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from database import get_db
import model, schema, utils, jwt_auth

router = APIRouter()

def user_exists(email: str = None, db: Session = Depends(get_db)):
    user = db.query(model.User).filter(model.User.email == email).first()
    return user

# Add middlewares
@router.get('/users/{email}', dependencies=[Depends(jwt_auth.JWTBearer())])
def read_user(email: str, db: Session = Depends(get_db)):
    
    if not email:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='User ID is required!')

    user = user_exists(email, db)

    if not user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='No user with this ID!')
    
    return user

@router.post('/register', status_code=status.HTTP_201_CREATED)
async def register_new_user(user: schema.UserRegister, db: Session = Depends(get_db)):

    if not user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Email and/or password are required to create an account!')

    if user_exists(user.email, db):
        return {"message": "User exists!"}
    
    # Hashing the new user password
    hashed_password = utils.hash(user.password)
    user.password = hashed_password

    # Add new user to the database
    new_user = model.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

# Add middlewares
@router.put('/information', dependencies=[Depends(jwt_auth.JWTBearer())])
def update_password(user_update: schema.UserUpdateInformation, db: Session = Depends(get_db)):

    if not user_update:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Email and Password are required to continue!')

    user_query = db.query(model.User).filter(model.User.email == user_update.email)
    user = user_query.first()

    if not user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='No user with this ID!')

    if utils.verify(user_update.password, user.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='User has set the same password!')
    
    hashed_password = utils.hash(user_update.password)
    user.password = hashed_password
    user_query.update(user_update.dict(exclude_unset=True), synchronize_session=False)
    db.commit()

    return {'message': 'Updated Password!'}
