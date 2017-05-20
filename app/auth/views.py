# -*- coding: utf-8 -*-
# app/auth/views.py

from flask import flash, redirect, render_template, url_for, request
from flask_login import login_required, login_user, logout_user

from . import auth
from forms import LoginForm
from .. import db
from ..models import User
from login import handle_login

@auth.route('/', methods=['GET', 'POST'])
def login():
    """
    Handle requests to the /login route
    Log an employee in through the login form
    """

    form = LoginForm()
    if form.validate_on_submit():
        # check whether user exists in the database and whether
        # the password entered matches the password in the database
        user = User.query.filter_by(username=form.username.data).first()
        if user is not None and user.verify_password(form.password.data):
            # log user in
            login_user(user)

            # redirect to the appropriate page
            if 'redirect_url' in request.args:
                return redirect(request.args['redirect_url'])
            return redirect(url_for('asset.assets'))
            # when login details are incorrect
        else:
            flash('Invalid username or password.')

     # load login template
    return render_template('auth/login.html', form=form, title='Login')

    ret = handle_login()
    if ret: return ret
    #in case the another url is to be used instead of the default one...
    if 'redirect_url' in request.args:
        return redirect(request.args['redirect_url'])
    return redirect(url_for('asset.assets'))


@auth.route('/logout')
@login_required
def logout():
    """
    Handle requests to the /logout route
    Log a user out through the logout link
    """
    logout_user()
    flash('You have successfully been logged out.')

    # redirect to the login page
    return redirect(url_for('auth.login'))

