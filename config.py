import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "afa9bec304152f1e369aa69c2199e3b9949e8fe9578f2183")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///site.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False