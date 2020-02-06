import os

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

DATABASE_URL = os.environ.get('DATABASE_URL', 'sqlite:////tmp/flask_app.db')

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
db = SQLAlchemy(app)


class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100))

  def __init__(self, name):
    self.name = name


@app.route('/', methods=['GET'])
def index():
  return render_template('index.html', users=User.query.all())

@app.route('/result/<username>', methods=['GET'])
def result(username):
  users=User.query.all()
  usernames = [user.name for user in users]
  registered = username in usernames

  u = User(username)
  db.session.add(u)
  db.session.commit()

  return render_template('index.html', users=User.query.all(), registered=registered)

@app.route('/user', methods=['POST'])
def user():
  username = request.form['name']
  return redirect(url_for('result', username=username))
  # # return redirect(url_for('index'))
  # return redirect(url_for('index'))

if __name__ == '__main__':
  db.create_all()
  port = int(os.environ.get('PORT', 5000))
  app.run(host='0.0.0.0', port=port, debug=True)
