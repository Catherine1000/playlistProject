from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
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
            Length(min=2, max=30)
        ]
    )
    album = StringField('Album',
        validators = [
            DataRequired(),
            Length(min=2, max=30)
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
    
    submit = SubmitField('Submit Playlist')

