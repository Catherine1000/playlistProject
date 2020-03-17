from application import db
from datetime import datetime



class Songs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), nullable=False)
    artist = db.Column(db.String(50), nullable=False)
    album = db.Column(db.String(50), nullable=False)
    

    def __repr__(self):
        return ''.join([
            'User ID: ', str(self.id), 'Song: ', self.title, ' ', 'Artist: ', self.artist, ' ', 'Album: ', self.album
            ])

class Playlists(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), nullable=False)
    genre = db.Column(db.String(50), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    

    def __repr__(self):
        return ''.join([
            'User ID: ', str(self.id), 'Title: ', self.title, ' ', 'Genre: ', self.genre
            ])

