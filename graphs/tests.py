from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status

import json

from .models import Graph

class GraphApiTest(TestCase):
    def setUp(self):
        Graph(name='ping', options='{"option1":"value"}').save()
        Graph(name='pong', options='{"o1":true, "o2":"fuck"}').save()
        self.user = User.objects.create_user(
            username='jacob', email='jacob@testing.com', password='testing!1234')
        self.client = APIClient()
        self.client.force_authenticate(self.user)

    def tearDown(self):
        Graph.objects.all().delete()
        self.user.delete()

    def test_get_list(self):
        response = self.client.get('/api/graph/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = json.loads(response.content)
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0]['name'], 'ping')
        self.assertEqual(data[0]['option1'], 'value')
        self.assertEqual(data[1]['o1'], True)

    def test_get_one(self):
        response = self.client.get('/api/graph/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = json.loads(response.content)
        self.assertEqual(data['name'], 'ping')
        self.assertEqual(data['option1'], 'value')

    def test_create_graph(self):
        response = self.client.post('/api/graph/', {'name': 'new', 'xaxi': 'xaxi'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        data = json.loads(response.content)
        self.assertIsNotNone(data.get('id', None))

    def test_update(self):
        response = self.client.put('/api/graph/1/', {'name':'peperoni', 'option3':'dalek!'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = json.loads(response.content)
        self.assertEqual(data['name'], 'peperoni')
        self.assertEqual(data['option3'], 'dalek!')

    def test_update(self):
        response = self.client.delete('/api/graph/1/', {'name':'peperoni', 'option3':'dalek!'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)