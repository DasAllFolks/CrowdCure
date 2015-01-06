from flask import Flask
from flask.ext.iniconfig import INIConfig


app = Flask(__name__)
INIConfig(app)


with app.app_context():
  app.config.from_inifile('settings.ini')
