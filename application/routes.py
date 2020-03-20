from flask import render_template, redirect, url_for
from application import app, db
from application.models import Songs, Playlists, playlistTracks
from application.forms import NewSongForm, NewPlaylistForm

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')

@app.route('/songs')
def songs():
    songData = Songs.query.all()
    return render_template('songs.html', title='Songs', songData=songData)

@app.route('/playlists')
def playlists():
    playlistData = Playlists.query.all()
    return render_template('playlists.html', title='Playlists', playlist=playlistData)

@app.route('/newsong', methods=['GET','POST'])
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

        return redirect(url_for('songs'))

    else:
        print(form.errors)

    return render_template('new_song.html', title='New Song', form=form)

@app.route('/newplaylist', methods=['GET','POST'])
def newplaylist():
    form = NewPlaylistForm()
    
    if form.validate_on_submit():
        playlist = Playlists(
            title = form.title.data,
            genre = form.genre.data
        )
        
        db.session.add(playlist)
        db.session.commit()

    
    
        return redirect(url_for('playlists'))

    else:
        print(form.errors)

    return render_template('new_playlist.html', title='New Playlist', form=form)


