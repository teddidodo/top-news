from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash(password: str):
    return pwd_context.hash(password)

def verify(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def return_the_date(time: str):

    # Convert the string to a datetime object
    timestamp = time.split(' ')[0]
    return timestamp

