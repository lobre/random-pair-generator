import os

DB_HOST = "db"
DB_PORT = "27017"
DB_NAME = "random-pair-generator"

APP_USER = "admin"
APP_PASS = "secret"

GIF_FILE = "loading.gif"

def upload_dir(filename):
    return os.path.join('static', 'upload', filename)
