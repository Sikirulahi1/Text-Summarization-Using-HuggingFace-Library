from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '30d2aa83a8e2a92845c0cd52a76f6aa3' # secrets.token_hex(16)

from summarizer import routes