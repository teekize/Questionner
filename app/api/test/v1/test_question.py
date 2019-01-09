import datetime
import unittest
from flask import jsonify, json
from app import createapp

class TestQuestionsEndpoint(unittest.TestCase):
    def setUp(self):
        self.app=createapp()
        self.app.testing=True
        self.client=self.app.test_client()
        self.q1={
            "id" : 1,#Integer,
            "createdOn" : datetime.datetime.utcnow(), #Date,
            "createdBy" : 1 ,# Integer, // represents the user asking the question
            "meetup" : 1, #integer, // represents the meetup the question is for
            "title" : "corruption",#String,
            "body" : "what is the main source of income",#String,
            "votes" : 0,#Integer,
        }
# val=self.q1['votes']
# val+=val       

    def test_question_post(self):
        '''tests the creation of a question method requires POST method'''
        response=self.client.post("/questions/", data=json.dumps(self.q1), content_type=("application/json"))
        results=json.loads(response.data.decode("utf-8"))
        self.assertEqual(results.status_code, 201)

    def test_question_patch_upvote(self):
        '''tests the updating of a question requires PATCH method'''
        response_1=self.client.post("/questions/", data=json.dumps(self.q1))
        results_1=json.loads(response_1.data.decode('utf-8'))
        results_id=results_1["id"]
        # resluts_vote=
        self.assertEqual(results_1.status_code, 201)

        response=self.client.patch("/questions/{}/upvote".format(results_id))
        results=json.loads(response.data.decode('utf-8'))
        self.assertEqual(results.status_code, 200)#the status code for updating

    def test_question_patch_downvote(self):
            '''tests the updating of a question requires the PATCH method'''
             
            response=self.client.post("/questions/", data=json.dumps(self.q1))
            results=json.loads(response.data.decode("utf-8"))
            results_id=results["id"]
            self.assertEqual(results.status_code, 201)

            response=self.client.patch("/questions/{}/downvote".format(results_id))
            results=json.loads(response.data.decode("utf-8"))
            self.assertEqual(results.status_code, 200)#the status code for updating


