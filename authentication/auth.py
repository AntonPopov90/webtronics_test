from fastapi import Depends
from fastapi_users.authentication import CookieTransport
from fastapi_users.authentication import JWTStrategy, AuthenticationBackend, BearerTransport
from config import SECRET_KEY
cookie_transport = CookieTransport(cookie_name='Webtronics',cookie_max_age=3600)

bearer_transport = BearerTransport(tokenUrl="auth/jwt/login")


SECRET = SECRET_KEY


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,
)
