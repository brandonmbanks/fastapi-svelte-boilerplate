import os
from passlib.context import CryptContext


class AuthHandler():
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    secret = os.getenv("SECRET_KEY")

    def verify_password(self, plain_password: str, hashed_password: str):
        return self.pwd_context.verify(plain_password, hashed_password)

    def generate_hashed_password(self, plain_password: str):
        return self.pwd_context.hash(plain_password)

    def encode_token(self, user_id: int):
        pass

    def decode_token(self, jwt: str):
        pass
