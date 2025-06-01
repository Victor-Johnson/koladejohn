import os 
from config import DevelopmentConfig,ProductionConfig,TestingConfig


def get_settings():
    env = os.getenv("ENV","development")
    if env == "production":
        return ProductionConfig()
    elif env == "testing":
        return TestingConfig()
    return DevelopmentConfig()

settings = get_settings()

