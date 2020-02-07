import os

from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

DATABASE_URL = os.environ.get('DATABASE_URL', 'sqlite:////tmp/flask_app.db')

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
db = SQLAlchemy(app)

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), unique=True)
  reserve_name = db.Column(db.String(100))

  def __init__(self, name, reserve_name):
    self.name = name
    self.reserve_name = reserve_name


@app.route('/', methods=['GET'])
def index():
  user = User.query.all()
  return render_template('index.html')

@app.route('/result/<username>', methods=['GET'])
def result(username):
   user = User.query.filter(User.name == username).all()
   registered = len(user) > 0
   reserve_name = ''
   if registered:
     reserve_name = user[0].reserve_name
   else:
    u = User(username, 'ジョイ')
    db.session.add(u)
    db.session.commit()

   return render_template('result.html', users=User.query.all(), registered=registered, reserve_name=reserve_name)

@app.route('/user', methods=['POST'])
def user():
  username = request.form['name']
  return redirect(url_for('result', username=username))

if __name__ == '__main__':
  # db.drop_all(bind=None)
  db.create_all()
  port = int(os.environ.get('PORT', 5000))
  app.run(host='0.0.0.0', port=port, debug=True)
