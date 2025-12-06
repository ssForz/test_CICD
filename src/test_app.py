import unittest
import sys
import os


import app as tested_app

class FlaskAppTests(unittest.TestCase):
    def setUp(self):
        tested_app.app.config['TESTING'] = True
        self.app = tested_app.app.test_client()
    
    def test_home_endpoint(self):
        r = self.app.get('/')
        res = b"""
    ====Simple Calculator====<br>
    Usage:<br>
    - /equation?&a=N&b=N&c=N - to solve ax^2 + bx + c = 0 equation<br>"""

        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.data, res)

    def test_equation_tworoots_endpoint(self):
        r = self.app.get('/equation?&a=2&b=3&c=1')
        res = b"""2.0*x^2 + 3.0*x + 1.0 = 0 <br><br>x1 = -1.0, x2 = -0.5"""

        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.data, res)
    
    def test_equation_oneroot_endpoint(self):
        r = self.app.get('/equation?&a=1&b=4&c=4')
        res = b"""1.0*x^2 + 4.0*x + 4.0 = 0 <br><br>x1,2 = -2.0"""

        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.data, res)
    
    def test_equation_imroots_endpoint(self):
        r = self.app.get('/equation?&a=1&b=-3&c=8.5')
        res = b"""1.0*x^2 - 3.0*x + 8.5 = 0 <br><br>x1 = 1.5 + (2.5)*i, x2 = 1.5 - (2.5)*i"""

        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.data, res)

if __name__ == "__main__":
    unittest.main()