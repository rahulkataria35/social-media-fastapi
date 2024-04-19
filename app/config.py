from pydantic_settings import BaseSettings

'''
Base class for settings, allowing values to be overridden by environment variables.
This is useful in production for secrets you do not wish to save in code, it plays nicely with docker(-compose),
Heroku and any 12 factor app design.
'''

class Settings(BaseSettings):
    database_hostname: str
    database_port: str
    database_password: str
    database_name: str
    database_username: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int
    
    class Config:
        env_file ='.env'

settings = Settings()