from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DB_HOST: str
    DB_PW: str
    DB_PORT: int
    DB_NAME: str
    DB_USER: str

    @property
    def psycopg_GET_DB(self):
        return f"postgresql+psycopg://{self.DB_USER}:{self.DB_PW}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()