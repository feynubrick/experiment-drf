import os


class EnvironmentVariableManager:
    def __init__(self):
        self.SECRET_KEY = os.environ.get("DJANGO_SECRET")
        self.DEBUG = os.environ.get("DJANGO_DEBUG") == "TRUE"


env_vars = EnvironmentVariableManager()
