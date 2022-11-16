import unittest

from app import app

class TestFlaskApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_index(self):
        res =  self.app.get('/test')
        assert res.status_code == 200
        expected = {'hello': 'world'}
        assert expected == json.loads(res.get_data(as_text=True))

    def test_hello_world_no_headers(self):
        res = self.app.get('/')
        self.assertEqual(res.status_code, 404)
        str_response = str(res.data)
        self.assertIn("<p>Sorry, Page not found</p>", str_response)

if __name__ == '__main__':
    unittest.main()

