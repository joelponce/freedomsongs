from project import db
from flask import render_template, redirect, request, url_for, Blueprint, flash
from project.songs.forms import SongForm
from project.models import Song
from project.users.views import ensure_correct_user
from flask_login import current_user, login_required

songs_blueprint = Blueprint(
    'songs',
    __name__,
    template_folder='templates'
)

@songs_blueprint.route('/', methods=['POST'])
def index(id):
    if current_user.get_id() == str(id):
        form = SongForm()
        if form.validate():
            new_song = Song(
                title = form.title.data,
                artist = form.artist.data,
                song_link = form.song_link.data,
                # tags = form.tags.data,
                user_id = id
            )
            db.session.add(new_song)
            db.session.commit()
            flash({'text': 'Thank you for contributing to the project. Your song was added to our database successfully!', 'status': 'success'})
            return redirect(url_for('home'))
    return render_template('songs/new.html', form=form)

@songs_blueprint.route('/new')
@login_required
@ensure_correct_user
def new(id):
    form = SongForm()
    return render_template('songs/new.html', form=form, user_id=id)

@songs_blueprint.route('/<int:song_id>', methods =['GET', 'DELETE'])
def show(id, song_id):
  found_song = Song.query.get(song_id)
  if request.method == b"DELETE" and current_user.get_id() == id:
    db.session.delete(found_song)
    db.session.commit()
    return redirect(url_for('songs.index', id=id))
  return render_template('songs/show.html', song=found_song)
