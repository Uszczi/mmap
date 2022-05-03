
from typing import Any, Dict

from pydantic import BaseSettings, PostgresDsn, validator


class Config(BaseSettings):
    DB_USER: str | None = None
    DB_PORT: str | None = None
    DB_PASSWORD: str | None = None
    DB_NAME: str | None = None
    DB_HOST: str | None = None

    SQLALCHEMY_DATABASE_URI: PostgresDsn | None

    @validator("SQLALCHEMY_DATABASE_URI", pre=True, always=True)
    def assemble_db_connection(
        cls, value: str | None, values: Dict[str, Any]
    ) -> str:
        if isinstance(value, str):
            db_url = value
        else:
            print(values)
            try:
                db_url = PostgresDsn.build(
                    scheme="postgresql",
                    user=values["DB_USER"],
                    password=values["DB_PASSWORD"],
                    host=values["DB_HOST"],
                    port=values["DB_PORT"],
                    path=f"/{values['DB_NAME']}",
                )
            except Exception as e:
                raise RuntimeError(
                    "Provide db credentials as DATABASE_URL or parts DB_HOST, DB_USER"
                ) from e
        return db_url

config = Config()
