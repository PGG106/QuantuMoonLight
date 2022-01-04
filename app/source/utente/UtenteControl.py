from flask import request, render_template
import hashlib
from flask_login import login_user, current_user, logout_user
from app import app, db
from app.models import Utente


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    """
Reads the user credentials from a http request and adds him to the project database
    :return: tbd
    """
    email = request.form.get('email')
    password = request.form.get('password')
    hashed_password = hashlib.sha512(password.encode()).hexdigest()
    token = request.form.get('token')
    username = request.form.get('username')
    nome = request.form.get('nome')
    cognome = request.form.get('cognome')
    utente = Utente(email=email, password=hashed_password, token=token, username=username, nome=nome, cognome=cognome)
    db.session.add(utente)
    db.session.commit()
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    reads a user login credentials from a http request and if they are valid logs the user in with those same
    credentials,changing his state from anonymous  user to logged user
    :return: tbd
    """
    email = request.form.get('email')
    password = request.form.get('password')
    hashed_password = hashlib.sha512(password.encode()).hexdigest()
    attempted_user: Utente = Utente.query.filter_by(email=email).first()
    if attempted_user.password == hashed_password:
        login_user(attempted_user)
    return render_template('index.html')


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    """
logs a user out, changing his state from logged user to anonymous user
    :return:tbd
    """
    logout_user()
    return render_template('index.html')
