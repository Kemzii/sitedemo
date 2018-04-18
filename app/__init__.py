from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'relufh382ewfidjo23i8ew'
from app import views