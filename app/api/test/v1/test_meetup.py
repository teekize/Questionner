import datetime
import unittest
from flask import jsonify, json
from app import createapp

class TestQuestionsEndpoint(unittest.TestCase):
    def setUp(self):
        self.app=createapp()
        self.app.testing=True
        self.client=self.app.test_client()
        self.date=datetime.datetime.utcnow()
        self.meetup={
            "id":1,#Integer,
            # "createdOn": "2019, 1, 9, 15, 30, 0,",#Date,
            "location":"nairobi", #String,
            "images" : "pintrest.png",#[String, String], // OPTIONAL: URL to the image location
            "topic" : "what is Andela",#String,
            "happeningOn" :"2019, 1, 9, 15, 30, 0,",#Date, // when the meetup is holding
            "Tags" : "dev"#[String, String, ....],

        }
# val=self.q1['votes']
# val+=val       

    def test_create_meetup(self):
        '''tests the creation of a meetup requires POST method'''
        response=self.client.post("/meetups/", data=json.dumps(self.meetup), content_type=("application/json"))
        results=json.loads(response.data.decode("utf-8"))
        self.assertEqual(results.status_code, 201)
        self.assertIn("nairobi", results)

    def test_get_one_meetup(self):
        '''tests method for getting a meetup requires PATCH method'''

        response=self.client.post("/meetups/", data=json.dumps(self.meetup), content_type=("application/json"))
        results=json.loads(response.data.decode("utf-8"))
        resluts_id=results["id"]
        self.assertEqual(results.status_code, 201)
        self.assertIn("nairobi", results)

        response_1=self.client.get("/meetups/{}/".format(resluts_id))
        results_1=json.loads(response_1.data.decode('utf-8'))
        self.assertEqual(results_1.status_code, 200)
        self.assertIn("what is andela", str(response_1))

        # response=self.client().patch("/questions/1/upvote", data=json.dumps({"vote":results_1["vote"]+1})
        # results=json.loads(response.data.decode('utf-8'))
        # self.assertEqual(results.status_code, 200)#the status code for updating

    def test_get_all_meetup(self):
            '''tests the method for gettting all meetups'''
            response_1=self.client.post("/meetups/", data=json.dumps(self.meetup), content_type=("application/json"))
            results_1=json.loads(response_1.data.decode("utf-8"))
            # resluts_id=results["id"]
            self.assertEqual(results_1.status_code, 201)
            self.assertIn("nairobi", str(results_1))
             
            response=self.client.get("/meetups/")
            results=json.loads(response.data.decode("utf-8"))
            self.assertEqual(results.status_code, 200)

            # response=self.client().patch("/questions/1/downvote", data=json.dumps({"votes":["votes"]-1}))
            # results=json.loads(response.data.decode("utf-8"))
            # assertEqual(results.status_code, )#the status code for updating


