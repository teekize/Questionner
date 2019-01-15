import datetime
import unittest
from flask import jsonify, json
from app import createapp 

class TestsForRsvp(unittest.TestCase):
    def setUp(self):
        '''sets ups the data to be used'''
        self.app= createapp()
        self.app.testing=True
        self.client=self.app.test_client()
        self.rsvp={
            "user" : 1,
            "response" : "yes"
        }
        self.meetup={
            
            "name":"teeka",
            "location":"nairobi", 
            "image" : "pintrest.png",
            "topic" : "what is Andela",
            "tag" : "dev",
            "happeningOn" : "2019-01-10 10:30"
            
        }

    def test_create_rsvp(self):
        '''tests the creation of an rsvp'''
        response = self.client.post("/api/v1/meetups", data = json.dumps(self.meetup),
                                                    content_type = "application/json")
        results = json.loads(response.data.decode())
        resluts_id = results["data"][0]["id"]
        self.assertEqual(response.status_code, 201)

        response_from_posting_rsvp = self.client.post("/api/v1/meetups/{}/rsvp".format(resluts_id), 
                                                                data = json.dumps(self.rsvp), 
                                                            content_type ="application/json")
        self.assertEqual(response_from_posting_rsvp.status_code, 201)


    def tearDown(self):
        '''Tears down the application after tests are done'''
        self.app = None