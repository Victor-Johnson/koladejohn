from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache

class BaseConfig(BaseSettings):
    db_model: str
    db_user: str
    db_password: str
    db_host: str
    db_port: int
    db_name: str
    secret_key: str
    algorithm: str

    @property
    def database_url(self):
        return f"{self.db_model}://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"

    model_config = SettingsConfigDict(env_file=".env") 


class DevelopmentConfig(BaseConfig):
    env: str = "development"


class ProductionConfig(BaseConfig):
    env: str = "production"


class TestingConfig(BaseConfig):
    env: str = "testing"