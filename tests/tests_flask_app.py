import unittest
import sys
import os
import json

# Ensure the root directory is in the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app

class TestFlaskApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_play_endpoint(self):
        response = self.app.post('/play', data=json.dumps({'choice': 'rock'}), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data(as_text=True))
        self.assertIn('user_choice', data)
        self.assertIn('computer_choice', data)
        self.assertIn('result', data)
        self.assertEqual(data['user_choice'], 'rock')

if __name__ == '__main__':
    unittest.main()