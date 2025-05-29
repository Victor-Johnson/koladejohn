from pydantic import BaseSettings


class Development(BaseSettings):
    env : str = "development"
    db_model : str 
    db_user : str 
    db_password : str 
    db_host : str 
    db_port: int 
    db_name: str 

    @property
    def database_url(self):
        return f"{self.db_model}://"
    



class Production(BaseSettings):
    pass


class Testing(BaseSettings):
    pass 
