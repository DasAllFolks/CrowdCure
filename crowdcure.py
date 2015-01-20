from contextlib import closing
import time

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
  # db = connect_db()
  # db.execute(
  #  'insert into locations (latitude, longitude, timestamp) values (?, ?, ?)',
  #  flask.request.form['latitude'],
  #  flask.request.form['longitude'],
  #  int(time.time()))
  # db.commit()
  # db.close()
  # return 'Database record should be created!'
  return 'Added the following to database: {latitude}, {longitude}'.format(
    latitude=flask.request.form['latitude'],
    longitude=flask.request.form['longitude'],
  )

@app.route('/test/', methods=['GET'])
def test_get():
  if flask.request.method == 'GET':
    return 'Successful GET\n'

@app.route('/test/', methods=['POST'])
def test_post():
  if flask.request.method == 'POST':
    return 'Successful POST\n'


## Debugging/running support.

if __name__ == '__main__':
  app.run()
