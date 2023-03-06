import os


class EnvironmentVariableManager:
    SECRET_KEY: str | None
    DEBUG: bool
    HOST: str
    PORT: str

    def __init__(self):
        self.SECRET_KEY = os.environ.get("DJANGO_SECRET")
        self.DEBUG = os.environ.get("DJANGO_DEBUG") == "TRUE"
        self.HOST = os.environ.get("DJANGO_HOST")
        self.PORT = os.environ.get("DJANGO_PORT")


env_vars = EnvironmentVariableManager()
