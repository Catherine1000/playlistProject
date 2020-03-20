from application import db
from datetime import datetime

playlistTracks = db.Table('playlistTracks',
    db.Column('song_id', db.Integer, db.ForeignKey('songs.song_id')),
    db.Column('playlist_id', db.Integer, db.ForeignKey('playlists.playlist_id'))
)

class Songs(db.Model):
    song_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), nullable=False)
    artist = db.Column(db.String(50), nullable=False)
    album = db.Column(db.String(50), nullable=False)
    playlists = db.relationship('Playlists', secondary='playlistTracks', lazy=True)
    

    def __repr__(self):
        return ''.join([
            'User ID: ', str(self.id), 'Song: ', self.title, ' ', 'Artist: ', self.artist, ' ', 'Album: ', self.album
            ])

class Playlists(db.Model):
    playlist_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), nullable=False)
    genre = db.Column(db.String(50), nullable=False)
    

    def __repr__(self):
        return ''.join([
            'User ID: ', str(self.id), 'Title: ', self.title, ' ', 'Genre: ', self.genre
            ])
