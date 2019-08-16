import json
import unittest
from shared import db
from template import app

class Test_Resource_Template(unittest.TestCase):
    ## Setup Functions
    def setUp(self):
        ## Take a copy of example.cfg and add the test database URI, or this will crash here
        app.config.from_pyfile('testing.cfg')
        self.app = app.test_client()
        with app.app_context():
            db.drop_all()
            db.create_all()

    def tearDown(self):
        pass

## Program main entry point
if __name__ == '__main__':
    unittest.main()