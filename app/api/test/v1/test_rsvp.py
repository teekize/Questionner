import datetime
import unittest
from flask import jsonify, json
from app import createapp 

class TestsForRsvp(unittest.TestCase):
    def setUp(self):
        self.app= createapp()
        self.app.testing=True
        self.client=self.app.test_client()
        self.rsvp={
            "id": 1,#Integer,
            "meetup": 1,#Integer,
            "user" : 1,#Integer, // represents the user
            "response" : "yes"#"yesString,
        }
        self.meetup={
            "id":1,#Integer,
            # "createdOn": "2019, 1, 9, 15, 30, 0,",#Date,
            "location":"nairobi", #String,
            "images" : "pintrest.png",#[String, String], // OPTIONAL: URL to the image location
            "topic" : "what is Andela",#String,
            "happeningOn" :"2019, 1, 9, 15, 30, 0,",#Date, // when the meetup is holding
            "Tags" : "dev"#[String, String, ....],

        }

    def test_create_rsvp(self):
        response=self.client.post("/api/v1/meetup", data=json.dumps(self.meetup), content_type="application/json")
        results=json.loads(response.data.decode())
        resluts_id=results["id"]
        self.assertEqual(results.status_code, 201)
        self.assertIn("nairobi", results)

        response=self.client.post("/api/v1/meetups/{}/rsvp".format(resluts_id), 
                                                                        data=json.dumps(self.rsvp), 
                                                                        content_type="application/json")
        results=json.loads(response.data.decode())
        self.assertEqual(results, 201)

if __name__ == "__main__":
    unittest.main()