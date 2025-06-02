import os 
from functools import lru_cache
from config import DevelopmentConfig,ProductionConfig,TestingConfig


@lru_cache()
def get_settings():
    env = os.getenv("ENV", "development")
    print(f"ENV = {env}")  
    settings_obj = None
    if env == "production":
        settings_obj = ProductionConfig()
    elif env == "testing":
        settings_obj = TestingConfig()
    else:
        settings_obj = DevelopmentConfig()

    print(f"Settings loaded: {settings_obj.dict()}") 
    return settings_obj
settings = get_settings()

