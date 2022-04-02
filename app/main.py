from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from dotenv import load_dotenv

from auth.handler import AuthHandler
from schemas import User

load_dotenv()

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

auth_handler = AuthHandler()

fake_users = {}


def get_user(email: str) -> User:
    if email in fake_users:
        return User(**fake_users[email])

# path operations are evaluated in order
# https://fastapi.tiangolo.com/tutorial/path-params/#order-matters


@app.get("/")
async def index():
    return {"message": "Hello World"}


@app.post("/register")
async def register():
    pass


@app.post("/login")
async def login():
    pass


@app.post("/token")
async def token(form_data: OAuth2PasswordRequestForm = Depends()):
    # lookup user in database
    user = get_user(form_data.username)
    if not user:
        raise HTTPException(status_code=400, detail="Invalid email or password")
    # check hashed password
    auth_handler.verify_password(form_data.password, user.hashed_password)
    # return jwt
