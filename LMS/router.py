from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

class UserCreate(BaseModel):
    username: str
    email: str
    password: str

@router.post("/register")
async def register_user(user: UserCreate):
    # Check if user already exists in the database
    if user.email in fake_users_db:
        raise HTTPException(status_code=400, detail="Email already registered")

    # Hash the password before storing it
    hashed_password = pwd_context.hash(user.password)

    # Add the new user to the fake database
    fake_users_db[user.email] = {
        "username": user.username,
        "email": user.email,
        "hashed_password": hashed_password,
        "disabled": False,
    }
    return {"message": "User registered successfully"}

@router.post("/login")
async def login_user(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user["email"]}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

from fastapi import Depends

@router.get("/protected-route")
async def protected_route(current_user: int = Depends(get_current_user)):
    return {"message": "You are authenticated"}
