import datetime
import unittest
from flask import jsonify, json
from .... import createapp

class TestQuestionsEndpoint(unittest.TestCase):
    def setUp(self):
        self.app = createapp()
        self.app.testing = True
        self.client = self.app.test_client()
        self.date = datetime.datetime.utcnow()
        self.meetup = {
          
            "name":"teeka",
            "location":"nairobi", 
            "images" : "pintrest.png",
            "topic" : "what is Andela",
            "tags" : "dev"
        }


    def test_create_meetup(self):
        '''tests the creation of a meetup requires POST method'''
        response = self.client.post("/api/v1/meetups", data = json.dumps(self.meetup), content_type="application/json")
        results = json.loads(response.data.decode("utf-8"))
        self.assertEqual(results.status_code, 201)
        self.assertIn("nairobi", str(results))

    def test_get_one_meetup(self):
        '''tests method for getting a meetup requires GET method'''

        response = self.client.post("/api/v1/meetups", data=json.dumps(self.meetup), content_type="application/json")
        results = json.loads(response.data.decode("utf-8"))
        resluts_id = results["id"]
        self.assertEqual(results.status_code, 201)
        self.assertIn("nairobi", results)

        response_1 = self.client.get("/api/v1/meetups/{}".format(resluts_id))
        results_1 = json.loads(response_1.data.decode('utf-8'))
        self.assertEqual(results_1.status_code, 200)
        self.assertIn("what is andela", str(response_1))

        

    def test_get_all_meetup(self):
            '''tests the method for gettting all meetups'''
            response_1 = self.client.post("/api/v1/meetups", data=json.dumps(self.meetup), content_type="application/json")
            results_1 = json.loads(response_1.data.decode("utf-8"))
            resluts_id = results_1["id"]
            self.assertEqual(results_1.status_code, 201)
            self.assertIn("nairobi", str(results_1))
             
            response = self.client.get("/api/v1/meetups/{}/upcoming".format(resluts_id))
            results = response.data.decode()
            self.assertEqual(results.status_code, 200)

         

