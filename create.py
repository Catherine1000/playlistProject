from application import db
from application.models import Songs, Playlists

db.drop_all()
db.create_all()