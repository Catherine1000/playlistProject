from flask import render_template
from application import app

@app.route('/')
@app.route('/home')
def home():
 return render_template('home.html', title='Home')


@app.route('/songs')
def songs():
    return render_template('songs.html', title='Songs')

@app.route('/playlists')
def playlists():
    return render_template('playlists.html', title='Playlists')