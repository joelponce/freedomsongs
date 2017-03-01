from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired

class SongForm(FlaskForm):
    title = StringField('Song Title', [InputRequired()])
    artist = StringField('Artist Name', [InputRequired()])
    # secondary_artist = StringField('Secondary Artist (optional)')
    song_link = StringField('Song Link', [InputRequired()])
    # tags = StringField('Song Tags', [InputRequired()])
