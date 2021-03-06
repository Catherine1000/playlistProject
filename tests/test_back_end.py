import unittest
from os import getenv
from flask import abort, url_for
from flask_testing import TestCase

from application import app, db
from application.models import Songs, Playlists
class TestBase(TestCase):

    def create_app(self):
        config_name = 'testing'
        app.config.update(
            SQLALCHEMY_DATABASE_URI=getenv('TEST_DATABASE')       )
        return app

    def setUp(self):
        db.session.commit()
        db.drop_all()
        db.create_all()
        
      
    def tearDown(self):

        db.session.remove()
        db.drop_all()

class TestViews(TestBase):
    
    def test_homepage(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)
    
    def test_createsong_page(self):
        response =self.client.get(url_for('newsong'))
        self.assertEqual(response.status_code, 200)
    
    def test_createplaylist_page(self):
        response =self.client.get(url_for('newplaylist'))
        self.assertEqual(response.status_code, 200)
    
    def test_playlists_page(self):
        response = self.client.get(url_for('playlists'))
        self.assertEqual(response.status_code, 200)