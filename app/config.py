from pydantic import BaseSettings



class Settings(BaseSettings):
    db_host: str
    db_port: str
    db_password: str
    db_username: str
    db_name: str

    secret_key: str
    algorithm: str
    access_token_expiration_minutes: int

    class Config:
        env_file = '.env'


settings = Settings()