from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter, Request
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from database import get_db
import model, schema, utils, jwt_auth

router = APIRouter()

@router.post('/login')
def login(user_credentials: schema.UserLogin, db: Session = Depends(get_db)):
    user = db.query(model.User).filter(
        model.User.email == user_credentials.email).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials")

    if not utils.verify(user_credentials.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials")

    # create a token
    access_token = jwt_auth.signJWT(user.id)

    return {'access_token': access_token, 'token_type': 'bearer'}