import unittest
import sys, os
import json
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import create_app

class TestUserEndpoints(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        import uuid
        unique_email = f"test.user.{uuid.uuid4()}@example.com"

        user1 = self.client.post('/api/v1/users/', json={
            "first_name": "Jane",
            "last_name": "Doe",
            "email": unique_email,
            "password": "azer1234"
        })
        self.valid_user = user1
        self.user_id = json.loads(user1.data.decode('utf-8'))['id']
        amenity1 = self.client.post('/api/v1/amenities/', json={
            "name": "Wi-Fi"
        })
        self.valid_amenity = amenity1
        self.amenity_id = json.loads(amenity1.data.decode('utf-8'))['id']
        place1 = self.client.post('/api/v1/places/', json={
            'title': 'MyPlace',
            'description': 'This is a place',
            'price': 34.65,
            'latitude': -30.56,
            'longitude': -56.67,
            'owner_id': self.user_id,
            'amenities': [self.amenity_id]
        })
        self.valid_place = place1
        self.place_id = json.loads(place1.data.decode('utf-8'))['id']
        print(f"Created place with ID: {self.place_id}")
        review1 = self.client.post('/api/v1/reviews/', json={
            "text": "Nice place",
            "rating": 4,
            "user_id": self.user_id,
            "place_id": self.place_id
        })
        self.valid_review = review1
        self.review_id = json.loads(review1.data.decode('utf-8'))['id']


    def tearDown(self):
        user_id = json.loads(self.valid_user.data.decode('utf-8'))
        amenity_id = json.loads(self.valid_amenity.data.decode('utf-8'))
        place_id = json.loads(self.valid_place.data.decode('utf-8'))
        review_id = json.loads(self.valid_review.data.decode('utf-8'))
        if hasattr(self, 'valid_review') and 'id' in review_id:
            self.client.delete(f'/api/v1/reviews/{review_id["id"]}')

        if hasattr(self, 'valid_place') and 'id' in place_id:
            self.client.delete(f'/api/v1/places/{place_id["id"]}')

        if hasattr(self, 'valid_amenity') and 'id' in amenity_id:
            self.client.delete(f'/api/v1/amenities/{amenity_id["id"]}')
    
        if hasattr(self, 'valid_user') and 'id' in user_id:
            self.client.delete(f'/api/v1/users/{user_id['id']}')


    def test_01_create_user(self):
        response = self.valid_user
        print(f"Response type: {type(response)}")
        print(f"Response data: {response}")
        print(f"Response status: {response.status_code}")
        self.assertEqual(response.status_code, 201)

    def test_02_create_user_invalid_data(self):
        response = self.client.post('/api/v1/users/', json={
            "first_name": "",
            "last_name": 12,
            "email": "john_legend@gmail.com",
            "password": "az4"
        })
        self.assertEqual(response.status_code, 400)


    def test_03_get_valid_user(self):
        response = self.client.get(f'/api/v1/users/{self.user_id}')
        self.assertEqual(response.status_code, 200)

    def test_04_get_invalid_user(self):
        response = self.client.get('/api/v1/users/1234')
        self.assertEqual(response.status_code, 404)

    def test_05_update_user_valid_data(self):
        response = self.client.put(f'/api/v1/users/{self.user_id}', json={
            "first_name": "Marie",
            "last_name": "Sue",
            "email": "marie.sue123@example.com",
            "password": "azer12345"
        })
        self.assertEqual(response.status_code, 200)

    def test_06_create_user_invalid_email(self):
        response = self.client.post('/api/v1/users/', json={
            "first_name": "marie",
            "last_name": "sue",
            "email": "marie.sue123@example.com",
            "password": "azer1234"
        })
        self.assertEqual(response.status_code, 409)

    def test_07_update_user_invalid_data(self):
        response = self.client.put(f'/api/v1/users/{self.user_id}', json={
            "first_name": "",
            "last_name": 12345,
            "email": "jane.doe@example.com",
            "password": "12r"
        })
        self.assertEqual(response.status_code, 400)

    def test_08_update_invalid_user(self):
        response = self.client.put('/api/v1/users/1234', json={
            "first_name": "Johnny",
            "last_name": "English",
            "email": "joeng@example.com",
            "password": "azer12345"
        })
        self.assertEqual(response.status_code, 404)

    def test_09_create_amenity_valid_data(self):
        response = self.client.post('/api/v1/amenities/', json={
            "name": "Wi-Fi"
        })
        self.assertEqual(response.status_code, 201)


    def test_10_create_amenity_invalid_data(self):
        response = self.client.post('/api/v1/amenities/', json={
            "name": 123
        })
        self.assertEqual(response.status_code, 400)

    def test_11_get_amenity_by_id(self):
        response = self.client.get(f'/api/v1/amenities/{self.amenity_id}')
        self.assertEqual(response.status_code, 200)

    def test_12_get_invalid_amenity(self):
        response = self.client.get('/api/v1/amenities/1234')
        self.assertEqual(response.status_code, 404)

    def test_13_get_all_amenities(self):
        response = self.client.get('/api/v1/amenities/')
        self.assertEqual(response.status_code, 200)

    def test_14_update_amenity_valid_data(self):
        response = self.client.put(f'/api/v1/amenities/{self.amenity_id}', json= {
            "name": "Air Conditioning"
        })
        self.assertEqual(response.status_code, 200)


    def test_15_update_amenity_invalid_data(self):
        response = self.client.put(f'/api/v1/amenities/{self.amenity_id}', json= {
            "name": 132
        })
        self.assertEqual(response.status_code, 400)


    def test_16_update_invalid_amenity(self):
        response = self.client.put('/api/v1/amenities/1234', json={
            "name": "Wi-Fi"
        })
        self.assertEqual(response.status_code, 404)


    def test_17_create_place_valid_data(self):
        """
        create place with data
        """
        response = self.client.post('/api/v1/places/', json={
            'title': 'NicePlace',
            'description': 'This is a valid place',
            'price': 34.65,
            'latitude': -30.56,
            'longitude': -56.67,
            'owner_id': self.user_id,
            'amenities': [self.amenity_id]
        })
        self.assertEqual(response.status_code, 201)


    def test_18_create_place_invalid_data(self):
        """
        test for create place with invalid data
        """
        response = self.client.post('/api/v1/places/', json={
            'title': '455',
            'description' 'invalid place'
            'price': 'grt',
            'latitude': '+30.56',
            'longitude':'bb/vB',
            'owner_id' : self.user_id,
            'amenities': [self.amenity_id]
        })
        self.assertEqual(response.status_code, 400)


    def test_19_get_all_place(self):
        response = self.client.get('/api/v1/places/')
        self.assertEqual(response.status_code, 200)


    def test_20_get_valid_place(self):
        response = self.client.get(f'/api/v1/places/{self.place_id}')
        self.assertEqual(response.status_code, 200)


    def test_21_get_invalid_place(self):
        response = self.client.get('/api/v1/places/invalid-id')
        self.assertEqual(response.status_code, 404)


    def test_22_update_place_valid_data(self):
        response = self.client.put(f'/api/v1/places/{self.place_id}', json={
            'title': 'Test Place',
            'description': 'Updated place',
            'price': 106,
            'latitude': 30.56,
            'longitude': 10.45,
            'owner_id': self.user_id,
            'amenities': [self.amenity_id]
        })
        self.assertEqual(response.status_code, 201)


    def test_23_update_place_invalid_data(self):
        """
        test updating place with invalid data
        """
        response = self.client.put(f'/api/v1/places/{self.place_id}', json={
            'title': 'Test Place',
            'description': 123,
            'price': -40,
            'latitude': 'hello',
            'longitude': 'world',
            'owner_id': self.user_id,
            'amenities': [self.amenity_id]
        })
        self.assertEqual(response.status_code, 400)


    def test_24_update_invalid_place(self):
        """
        test  updating places if invalid
        """
        response = self.client.put('/api/v1/places/invalid-id', json={
            'title': 'Updated Title',
        })
        self.assertEqual(response.status_code, 404)


    def test_25_create_review_valid_data(self):
        response = self.client.post('/api/v1/reviews/', json={
            'text': 'great place',
            'rating': 4,
            'user_id': self.user_id,
            'place_id': self.place_id
        })
        self.assertEqual(response.status_code, 201)


    def test_26_create_review_invalid_data(self):
        response = self.client.post('/api/v1/reviews/', json={
            'text': 123,
            'rating': 12,
            'user_id': self.user_id,
            'place_id': self.place_id
        })
        self.assertEqual(response.status_code, 400)

    # 10 
    def test_27_get_valid_review(self):
        response = self.client.get(f'/api/v1/reviews/{self.review_id}')
        self.assertEqual(response.status_code, 200)

    def test_28_get_invalid_review(self):
        response = self.client.get('/api/v1/reviews/456789')
        self.assertEqual(response.status_code, 404)

    def test_29_get_all_reviews(self):
        response = self.client.get('/api/v1/reviews/')
        self.assertEqual(response.status_code, 200)
    
    def test_30_get_reviews_by_valid_place(self):
        known_place_id = self.place_id
        print(f"Testing with place_id: {self.place_id}")
        url = f'/api/v1/places/{self.place_id}/reviews'
        print(f"Request URL: {url}")
        response = self.client.get(url)
        print(f"Response status: {response.status_code}")
        print(f"Response data: {response.data}")
        response = self.client.get(f'/api/v1/places/{known_place_id }/reviews')
        self.assertEqual(response.status_code, 200)

    def test_31_get_reviews_by_invalid_place(self):
        response = self.client.get('/api/v1/places/1234567/reviews')
        self.assertEqual(response.status_code, 404)

    def test_32_update_review_valid_data(self):
        response = self.client.put(f'/api/v1/reviews/{self.review_id}', json={
            "text": "Bad place",
            "rating": 2,
            "user_id": self.user_id,
            "place_id": self.place_id
        })
        self.assertEqual(response.status_code, 200)

    def test_33_update_review_invalid_data(self):
        response = self.client.put(f'/api/v1/reviews/{self.review_id}', json={
            "text": 1234,
            "rating": 12,
            "user_id": self.user_id,
            "place_id": self.place_id
        })
        self.assertEqual(response.status_code, 400)

    def test_34_update_invalid_review(self):
        response = self.client.put('/api/v1/reviews/IDinvalid', json={
            "text": "Nice review",
            "rating": 4,
            "user_id": self.user_id,
            "place_id": self.place_id
        })
        self.assertEqual(response.status_code, 404)

    def test_35_delete_valid_review(self):
        response = self.client.delete(f'/api/v1/reviews/{self.review_id}')
        self.assertEqual(response.status_code, 200)

    def test_36_delete_invalid_review(self):
        response = self.client.delete('/api/v1/reviews/invalidreviewID')
        self.assertEqual(response.status_code, 404)


if __name__ == "__main__":
    unittest.main()
