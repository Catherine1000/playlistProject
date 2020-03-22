from flask import render_template, redirect, url_for, request
from application import app, db
from application.models import Songs, Playlists
from application.forms import NewSongForm, NewPlaylistForm

@app.route('/')
@app.route('/home')
def home():
    songs = Songs.query.all()
    return render_template('home.html', title='Home', songs=songs)


@app.route('/playlists')
def playlists():
    playlists = Playlists.query.all()
    return render_template('playlists.html', title='My Playlists', playlists=playlists)

@app.route('/songs/new', methods=['GET','POST'])
def newsong():
    form = NewSongForm()
    if form.validate_on_submit():
        song = Songs(
            title = form.title.data,
            artist = form.artist.data,
            album = form.album.data
        )
        db.session.add(song)
        db.session.commit()
        return redirect(url_for('home'))
    else:
        print(form.errors)
    return render_template('new_song.html', title='New Song', form=form)

@app.route('/songs/<int:song_id>')
def song(song_id):
    song = Songs.query.get(song_id)
    return render_template('song.html', song=song)

@app.route('/songs/<int:song_id>/update', methods=['GET','POST'])
def update_song(song_id):
    song = Songs.query.get(song_id)
    form = NewSongForm()
    if form.validate_on_submit():
        song.title = form.title.data
        song.artist = form.artist.data
        song.album = form.album.data
        db.session.commit()
        return redirect(url_for('song', song_id=song.song_id))
    elif request.method == 'GET':
        form.title.data = song.title
        form.artist.data = song.artist
        form.album.data = song.album
    return render_template('new_song.html', title='Update Song', form=form)

@app.route('/playlist/new', methods=['GET','POST'])
def newplaylist():
    form = NewPlaylistForm()
    form.song.choices=[(song.song_id, song.title) for song in Songs.query.all()]
    if form.validate_on_submit():
        playlist = Playlists(
            title = form.title.data,
            genre = form.genre.data,
            song_id = form.song.data
        )
        
        db.session.add(playlist)
        db.session.commit()
        return redirect(url_for('playlists'))
    else:
        print(form.errors)
    return render_template('new_playlist.html', title='My Playlist', form=form)

@app.route('/playlists/<int:playlist_id>')
def playlist(playlist_id):
    playlist = Playlists.query.get(playlist_id)
    return render_template('playlist.html', playlist=playlist)

@app.route('/playlists/<int:playlist_id>/delete', methods=['POST'])
def delete_playlist(playlist_id):
    playlist = Playlists.query.get(playlist_id)
    db.session.delete(playlist)
    db.session.commit()
    return redirect(url_for('playlists'))