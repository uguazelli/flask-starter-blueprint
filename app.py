from flask import Flask
from api.api import api_blueprint
from login.login import login_blueprint

app = Flask(__name__)
app.register_blueprint(api_blueprint)
app.register_blueprint(login_blueprint)
