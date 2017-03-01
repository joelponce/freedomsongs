import datetime
from project import db, bcrypt
from flask_login import UserMixin

# SongTag = db.Table('songs_tags',
#                     db.Column('id',
#                                db.Integer,
#                                primary_key=True),
#                     db.Column('song_id',
#                               db.Integer,
#                               db.ForeignKey('songs.id',
#                               ondelete='cascade')),
#                     db.Column('tag_id',
#                               db.Integer,
#                               db.ForeignKey('tags.id',
#                               ondelete='cascade')),
#                    )

class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text, unique=True)
    email = db.Column(db.Text, unique=True)
    password = db.Column(db.Text)
    first_name = db.Column(db.Text)
    last_name = db.Column(db.Text)
    registered_on = db.Column(db.DateTime, nullable=False)
    admin = db.Column(db.Boolean, nullable=False, default=False)
    songs = db.relationship('Song', backref='user', lazy='dynamic')

    # Future update: email verification
    # confirmed = db.Column(db.Boolean, nullable=False, default=False)
    # confirmed_on = db.Column(db.DateTime, nullable=True)

    def __init__(self, username, email, password, first_name, last_name, admin=False):
        self.username = username
        self.email = email
        self.password = bcrypt.generate_password_hash(password).decode('UTF-8')
        self.first_name = first_name
        self.last_name = last_name
        self.registered_on = datetime.datetime.now()
        self.admin = admin

        # Future update: email verification
        # self.confirmed = confirmed
        # self.confirmed_on = confirmed_on


class Song(db.Model):
    __tablename__ = 'songs'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    artist = db.Column(db.Text)
    song_link = db.Column(db.Text)
    date_added = db.Column(db.DateTime, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    # tags = db.relationship('Tag',
    #                        secondary=SongTag,
    #                        backref=db.backref('tags', lazy='dynamic'))

    def __init__(self, title, artist, song_link, user_id):
        self.title = title
        self.artist = artist
        self.song_link = song_link
        self.date_added = datetime.datetime.now()
        self.user_id = user_id


# class Tag(db.Model):
#     __tablename__ = 'tags'
#
#     id = db.Column(db.Integer, primary_key=True)
#     tag = db.Column(db.Text)
