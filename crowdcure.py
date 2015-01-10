from contextlib import closing

from flask import Flask
from flask.ext.iniconfig import INIConfig
import sqlite3


app = Flask(__name__)
INIConfig(app)


with app.app_context():
  app.config.from_inifile('settings.ini')

def connect_db():
  return sqlite3.connect(app.config['database']['DATABASE'])

def init_db():
  with closing(connect_db()) as db:
    with app.open_resource('schema.sql', mode='r') as f:
      db.cursor().executescript(f.read())
    db.commit()

if __name__ == '__main__':
  app.run()
