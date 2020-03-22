from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, ValidationError

class NewSongForm(FlaskForm):
    title = StringField('Title',
        validators = [
            DataRequired(),
            Length(min=2, max=30)
        ]
    )
    artist = StringField('Artist',
        validators = [
            DataRequired(),
            Length(min=2, max=50)
        ]
    )
    album = StringField('Album',
        validators = [
            DataRequired(),
            Length(min=2, max=50)
        ]
    )
    
    submit = SubmitField('Done')
    

class NewPlaylistForm(FlaskForm):
    title = StringField('Title',
        validators = [
            DataRequired(),
            Length(min=2, max=30)
        ]
    )
    genre = StringField('Genre',
        validators = [
            DataRequired(),
            Length(min=2, max=30)
        ]
    )
    song = SelectField('Song', coerce=int)
    
    submit = SubmitField('Submit Playlist')


