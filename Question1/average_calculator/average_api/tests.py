from django.test import TestCase, Client
import json

class AverageCalculatorTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_valid_input(self):
        payload = {'numbers': [10, 20, 30, 40, 50]}
        response = self.client.post(
            '/api/calculate/',
            data=json.dumps(payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'average': 30.0})

    def test_empty_list(self):
        payload = {'numbers': []}
        response = self.client.post(
            '/api/calculate/',
            data=json.dumps(payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {'error': 'The list of numbers cannot be empty.'})

    def test_invalid_input(self):
        payload = {'numbers': [10, 'twenty', 30]}
        response = self.client.post(
            '/api/calculate/',
            data=json.dumps(payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {'error': 'All elements in the list must be numbers.'})

    def test_non_list_input(self):
        payload = {'numbers': '10, 20, 30'}
        response = self.client.post(
            '/api/calculate/',
            data=json.dumps(payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {'error': 'Input must be a list of numbers.'})