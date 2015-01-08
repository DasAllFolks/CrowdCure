from flask import Flask
from flask.ext.iniconfig import INIConfig
import sqlite3


app = Flask(__name__)
INIConfig(app)


with app.app_context():
  app.config.from_inifile('settings.ini')

def connect_db():
  return sqlite3.connect(app.config['database']['DATABASE'])

if __name__ == '__main__':
  app.run()
