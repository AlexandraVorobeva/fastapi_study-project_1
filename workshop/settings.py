from pydantic import BaseSettings

class Settings(BaseSettings):
    server_host: str = '127.0.0.1'
    server_port: int = 8000
    # database_url: str

    jwt_secret: str = 'o9A-elwuIGHLAPu20Qz94AKzJpEad5U_u3HWIYXiOmU'
    jwt_algorithm: str = 'H5256'
    jwt_expiration: int = 3600


settings = Settings(
    _env_file='../.env',
    _env_file_encoding='utf-8',
)