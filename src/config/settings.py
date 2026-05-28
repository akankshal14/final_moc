from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DB_DIALECT:str
    DB_USERNAME:str
    DB_PASSWORD:str
    DB_NAME:str
    DB_HOST:str
    DB_PORT:int
    SECRET_KEY:str
    ALGORITHM:str
    ACCESS_TOKEN_EXPIRE_MINUITES:int
    REFRESH_TOKEN_EXPIRE_DAYS:int
    
    SUPERADMIN_SALUTATION:str
    SUPERADMIN_FIRST_NAME:str
    SUPERADMIN_LAST_NAME:str
    SUPERADMIN_EMAIL:str
    SUPERADMIN_PASSWORD:str

    AWS_ACCESS_KEY_ID: str
    AWS_SECRET_ACCESS_KEY: str
    AWS_REGION_NAME: str
    AWS_BUCKET_NAME: str
    class Config:
        env_file=".env"
    def get_database_url(self):
        return f"{self.DB_DIALECT}://{self.DB_USERNAME}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

settings=Settings()