import unittest
from unittest.mock import patch
from app import app, prediction

class TestApp(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_home_page(self):
        response = self.app.get('/')
        #print(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Please copy artical here', response.data)

    @patch('builtins.print')
    def test_prediction(self, mock_print):
        test_text = "Hello, there folks today we are going to contribute contribution contributed like likes likely liked i dont care anymore!!!"
        expected_output = ['hello', 'folk', 'today', 'go', 'contribut', 'contribut', 'contribut', 'like', 'like', 'like', 'like', 'dont', 'care', 'anymor']
        prediction(test_text)
        mock_print.assert_called_with(expected_output)

if __name__ == '__main__':
    unittest.main()