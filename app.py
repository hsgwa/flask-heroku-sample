import os

from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from spread_sheet import get_list
from guest import Guest, Guests

app = Flask(__name__)
guests = Guests()


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/result/<username>', methods=['GET'])
def result(username):
    guests.update()

    users = guests.get_guests()
    registered = guests.is_exist(username)
    user = guests.get_guest(username)

    return render_template('result.html', users=users,
                           registered=registered, user=user)


@app.route('/user', methods=['POST'])
def user():
    username = request.form['name']
    return redirect(url_for('result', username=username))


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
