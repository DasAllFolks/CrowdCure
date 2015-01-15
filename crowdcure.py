from contextlib import closing

import flask
from flask.ext.iniconfig import INIConfig
import sqlite3


## Setup and config.

app = flask.Flask(__name__)
INIConfig(app)

with app.app_context():
  app.config.from_inifile('settings.ini')


## Database stuff.

def connect_db():
  return sqlite3.connect(app.config['database']['DATABASE'])

def init_db():
  with closing(connect_db()) as db:
    with app.open_resource('schema.sql', mode='r') as f:
      db.cursor().executescript(f.read())
    db.commit()


## Views.

@app.route('/create-report/', methods=['GET'])
def create_report_get():
  return flask.render_template('create_report.html')

@app.route('/create-report/', methods=['POST'])
def create_report_post():
  db = connect_db()
  # XXXX: And then I suppose create the database record here?
  db.close()

@app.route('/test/', methods=['GET'])
def test_get():
  if request.method == 'GET':
    return 'Successful GET\n'

@app.route('/test/', methods=['POST'])
def test_post():
  if request.method == 'POST':
    return 'Successful POST'


## Debugging/running support.

if __name__ == '__main__':
  app.run()
