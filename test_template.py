import json
import unittest
from shared import db
from template import app

class UnitTest_Template(unittest.TestCase):
    ## Setup Functions
    def setUp(self):
        app.config.from_pyfile('testing.cfg')   ## Take a copy of example.cfg and add the test database URI, or this will crash here
        self.app = app.test_client()
        with app.app_context():
            db.create_all()
    ## Teardown
    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

class FeatureTest_Template(unittest.TestCase):
    ## Setup Functions
    def setUp(self):
        app.config.from_pyfile('testing.cfg')   ## Take a copy of example.cfg and add the test database URI, or this will crash here
        self.app = app.test_client()
        with app.app_context():
            db.create_all()
    ## Teardown
    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

## Program main entry point
if __name__ == '__main__':
    unittest.main()