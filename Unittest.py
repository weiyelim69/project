import unittest
import requests
import DA_Team_3
class Test(unittest.TestCase):

    def test_successful(self):
        url = 'http://wikipedia.org'
        r = requests.get(url)
        self.assertEqual(r.status_code, 200)

if __name__ == '__main__':
    unittest.main()
