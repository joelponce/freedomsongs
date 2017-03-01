from project import db, bcrypt
from flask import render_template, redirect, request, url_for, Blueprint, flash
from project.users.forms import UserForm, LoginForm
from project.models import User
from flask_login import login_user, logout_user, current_user, login_required
from sqlalchemy.exc import IntegrityError
from functools import wraps

users_blueprint = Blueprint(
    'users',
    __name__,
    template_folder='templates'
)

def ensure_correct_user(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if kwargs.get('id') != current_user.id:
            flash({'text': "Not Authorized", 'status': 'danger'})
            return redirect(url_for('home'))
        return fn(*args, **kwargs)
    return wrapper

@users_blueprint.route('/about')
def about():
    return render_template('users/about.html')

@users_blueprint.route('/faq')
def faq():
    return render_template('users/faq.html')

@users_blueprint.route('/signup', methods=['GET', 'POST'])
def signup():
    form = UserForm()
    if request.method == 'POST':
        if form.validate():
            try:
                new_user = User(
                    username=form.username.data,
                    email=form.username.data,
                    password=form.password.data,
                    first_name=form.first_name.data,
                    last_name=form.last_name.data
                )
                db.session.add(new_user)
                db.session.commit()
                login_user(new_user)
            except IntegrityError as e:
                flash({'text': "Username already taken", 'status': 'danger'})
                return render_template('users/signup.html', form=form)
            return redirect(url_for('home'))
    return render_template('users/signup.html', form=form)

@users_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        if form.validate():
            found_user = User.query.filter_by(username=form.username.data).first()
            if found_user:
                is_authenticated = bcrypt.check_password_hash(found_user.password, form.password.data)
                if is_authenticated:
                    login_user(found_user)
                    flash({'text': 'Welcome, {}!'.format(found_user.first_name), 'status': 'success'})
                    return redirect(url_for('home'))
            flash({'text': "Invalid credentials.", 'status': 'danger'})
            return render_template('users/login.html', form=form)
    return render_template('users/login.html', form=form)

@users_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    flash({ 'text': "You have successfully logged out.", 'status': 'success' })
    return redirect(url_for('users.login'))

@users_blueprint.route('/<int:id>/account', methods=['GET', 'PATCH', 'DELETE'])
@login_required
@ensure_correct_user
def account(id):
    user = User.query.get(id)
    form = UserForm()
    return render_template('users/account.html', form=form, user=user)

@users_blueprint.route('/<int:id>', methods=["GET", "PATCH", "DELETE"])
@login_required
def show(id):
  found_user = User.query.get(id)
  if request.method == 'GET' or current_user.is_anonymous or current_user.get_id() != str(id):
    return render_template('users/show.html', user=found_user)
  if request.method == b"PATCH":
    form = UserForm(request.form)
    if form.validate():
      if bcrypt.check_password_hash(found_user.password, form.password.data):
        found_user.username = form.username.data
        found_user.email = form.email.data
        db.session.add(found_user)
        db.session.commit()
        return redirect(url_for('users.show', id=id))
      flash({ 'text': "Wrong password, please try again.", 'status': 'danger'})
    return render_template('users/edit.html', form=form, user=found_user)
  if request.method == b"DELETE":
    db.session.delete(found_user)
    db.session.commit()
    return redirect(url_for('users.signup'))
