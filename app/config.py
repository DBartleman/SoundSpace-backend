import os


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "key-for-devs"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    # SQLALCHEMY_DATABASE_URI = "postgresql://soundspace_user:password@localhost/soundspace_db"
