from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    debug_logs: str = ""
    database_url: str = "postgresql+asyncpg://postgres:postgres@postgres:5432/swarmica"
    echo_sql: bool = True
    test: bool = False
    project_name: str = "Swarmica"


settings = Settings()  # type: ignore
