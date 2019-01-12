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
            "tags" : "dev",
            "happeningOn" : "2019-1-10"
        }

        self.meetup2 = {
          
            "name":"teeka",
            "location":"nairobi", 
            "images" : "pintrest.png",
            "tags" : "dev",
            "happeningOn" : "2019-1-10"
        }

    def post_meetup(self):
        response=self.client.post("/api/v1/meetups", data = json.dumps(self.meetup),
                                                    content_type = "application/json")
        return response

    def test_create_meetup(self):
        '''tests the creation of a meetup requires POST method'''
        response = self.client.post("/api/v1/meetups", 
                                                        data = json.dumps(self.meetup), 
                                                        content_type="application/json")

        self.assertEqual(response.status_code, 201)
    
    def test_no_topic(self):
        '''test where no topic is given'''
        response = self.client.post("/api/v1/meetups", 
                                                        data = json.dumps(self.meetup2), 
                                                        content_type="application/json")                                             
        self.assertEqual(response.status_code, 204)


    def test_get_one_meetup(self):
        '''tests  getting a specific meetup requires GET method'''
        response = self.post_meetup()
        results = json.loads(response.data.decode())
        resluts_id = results["data"][0]["id"]
        self.assertEqual(response.status_code, 201)
        
        response_1 = self.client.get("/api/v1/meetups/{}".format(resluts_id))
        self.assertEqual(response_1.status_code, 200)
        

        

    def test_get_all_meetup(self):
            '''tests the for gettting all upcoming  meetups'''
            response = self.post_meetup()
            self.assertEqual(response.status_code, 201)
           
            response_1 = self.client.get("/api/v1/meetups/upcoming")
            self.assertEqual(response_1.status_code, 200)

         

