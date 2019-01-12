import datetime
import unittest
from flask import jsonify, json
from .... import createapp

class TestQuestionsEndpoint(unittest.TestCase):
    def setUp(self):
        self.app = createapp()
        self.app.testing = True
        self.client = self.app.test_client()
        self.q1 = {
            
            "createdBy" : "teeka",
            "body" : "why is life unfair",
            "title" : "life",
            "meetup" : 1,
            
        }
    def post_question(self):
        response = self.client.post("/api/v1/questions",
                                                        data = json.dumps(self.q1),
                                                        content_type = "application/json")
        return response

    def test_question_post(self):
        '''tests the creation of a question '''
        response = self.post_question()
        self.assertEqual(response.status_code, 201)

    def test_question_patch_upvote(self):
        '''tests the updating of a question requires PATCH method'''
        response_1 = self.post_question()
        results_1 = json.loads(response_1.data.decode())
        results_id = results_1["data"][0]["id"]
        self.assertEqual(response_1.status_code, 201)

        response = self.client.patch("/api/v1/questions/{}/upvote".format(results_id))
        self.assertEqual(response.status_code, 201)

    def test_question_patch_downvote(self):
            '''tests the updating of a question requires the PATCH method'''
            response = self.post_question()
            results = json.loads(response.data.decode())
            results_id = results["data"][0]["id"]
            self.assertEqual(response.status_code, 201)

            response_1 = self.client.patch("/api/v1/questions/{}/downvote".format(results_id))
            results = response.data.decode()
            self.assertEqual(response_1.status_code, 201)

