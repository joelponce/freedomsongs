from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_modus import Modus
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost/freedomsongs-db'
app.config['SQALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

modus = Modus(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
db = SQLAlchemy(app)

from project.users.views import users_blueprint
from project.songs.views import songs_blueprint
from project.models import User, Song

app.register_blueprint(users_blueprint, url_prefix='/users')
app.register_blueprint(songs_blueprint, url_prefix='/users/<int:id>/songs')

@app.route('/')
def home():
    songs = Song.query.order_by("date_added asc").limit(10).all()
    return render_template('home.html', songs=songs)

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))
