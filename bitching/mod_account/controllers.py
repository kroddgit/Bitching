import sys
import os
from flask import (
    Blueprint,
    flash,
    g,
    redirect,
    render_template,
    request,
    session,
    url_for
)
from flask_wtf import (
    Form,
)
from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)
from flask_login import (
    current_user,
    login_required,
    login_user,
    logout_user,
)
from bitching.mod_account.forms import (
    LoginForm,
    RegisterForm
)

from bitching.mod_account.models import (
    User
)

from bitching import db

mod_account = Blueprint('account', __name__, url_prefix='/bitch')

@mod_account.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        loginUser = User.query.filter_by(username=form.user_name.data).first()
        if loginUser is None:
            flash("User does not exist", "alert-danger")
            return redirect(url_for("account.login"))
        else:
            print "login:",loginUser.password,":", loginUser.username
            print form.password.data
            print generate_password_hash(form.password.data)
            if check_password_hash(loginUser.password, form.password.data):
                loginUser.is_authenticated(True)
                login_user(loginUser)
                return redirect(url_for("bitch.home"))
            else:
                flash("Bad Username or Password", "alert-danger")
                return redirect(url_for("account.login"))
    else:
        if current_user.is_authenticated:
            return redirect(url_for("bitch.home"))
        else:
            return render_template('account/login.html', form=form)
@mod_account.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        exists = User.query.filter_by(username=form.username.data).first()
        if exists is not None:
            print exists.username, exists.email
            flash("Someone already snagged that user name.... sorry", "alert-danger")
            return redirect(url_for("account.register"))

        emailUsed = User.query.filter_by(email=form.email.data).first()
        if emailUsed is not None:
            print emailUsed.username, emailUsed.email
            flash("That email is already in use, that sucks","alert-danger")
            return redirect(url_for("account.register"))

        if form.password.data != form.retype.data:
            flash("Password's don't match dumb dumb!","alert-danger")
            return redirect(url_for("account.register"))

        hash = generate_password_hash(form.password.data)
        newUser = User(form.username.data, form.email.data, hash, True, "blue")
        newUser.is_authenticated(True)
        db.session.add(newUser)
        db.session.commit()
        login_user(newUser)
        return redirect(url_for("bitch.home"))
    else:
        return render_template('account/register.html', form=form)

@mod_account.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("account.login"))
