from dataclasses import dataclass
from environs import Env
from typing import Optional

@dataclass
class DatabaseConfig:
    database_url: str
    echo: bool = False

@dataclass
class Config:
    db: DatabaseConfig
    debug: bool
    app_host: str = "0.0.0.0"
    app_port: int = 8000

def load_config(path: Optional[str] = None) -> Config:
    env = Env()
    env.read_env(path)

    return Config(
        db=DatabaseConfig(
            database_url=env.str("DATABASE_URL"),
            echo=env.bool("DB_ECHO", default=False)
        ),
        debug=env.bool("DEBUG", default=False)
    )
