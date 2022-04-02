from auth.handler import AuthHandler


def test_it_can_hash_a_password():
    auth_handler = AuthHandler()
    plain_password = "password123"
    hashed_password = auth_handler.generate_hashed_password(plain_password)
    assert auth_handler.verify_password(plain_password, hashed_password)
