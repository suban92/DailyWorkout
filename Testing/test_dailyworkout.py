import unittest
from flask import url_for
from flask_testing import TestCase
from app import app, db, daily_workout
class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URL="sqlite:///")
        app.config['SECRET_KEY'] = 'Xconcept7'
        return app


    def setUp(self):
        db.create_all()
        workout_1 = daily_workout(id=1, title = "pullup", complete= False)
        db.session.add
        db.session.commit()

    def teardown(self):
        db.drop_all()



class Testpages(TestBase):
    def testHomepage(self):
        response = self.client.get(url_for("index"))
        self.assertEqual(response.status_code, 200)
        
    def testadd(self):
        response = self.client.post("add/2")
        self.assertIn(b"2", response.data) 

    def testdelete(self):
        response = self.client.get("delete/1")
        self.assertEqual(response.status_code, 405)
    
    def testdone(self):
        response = self.client.post("done/1")
        self.assertIn(b"1", response.data)

#    def testdelete2(self):
 #       response = self.client.post("delete/1")
  #      data = daily_workout(id=1)
   #     follow_redirects=True
    #    self.assertEqual(response.status_code, 200)
        
