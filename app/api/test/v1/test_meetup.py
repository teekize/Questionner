import datetime
import unittest
from flask import jsonify, json
from .... import createapp

class TestQuestionsEndpoint(unittest.TestCase):
    def setUp(self):
        '''setup the data and application that will be used'''
        self.app = createapp()
        self.app.testing = True
        self.client = self.app.test_client()
        self.meetup = {
          
            "name":"teeka",
            "location":"nairobi", 
            "image" : "pintrest.png",
            "topic" : "what is Andela",
            "tag" : "dev",
            "happeningOn" : "2019-01-10 10:30"
            
        }
        self.meetup_invalid_date = {
          
            "name":"teeka",
            "location":"nairobi", 
            "image" : "pintrest.png",
            "topic" : "what is Andela",
            "tag" : "dev",
            "happeningOn" : "2019-30-01"
        }
        self.meetup_not_string = {
          
            "name":1,
            "location":"nairobi", 
            "image" : "pintrest.png",
            "topic" : "what is Andela",
            "tag" : "dev",
            "happeningOn" : "2019-01-30"
        }

        self.meetup_incorrect = {
          
            "name":"teeka",
            "location":"nairobi", 
            "image" : "pintrest.png",
            "tag" : "dev",
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
    
    def test_no_mising_one_field(self):
        '''test where one field is missing '''
        response = self.client.post("/api/v1/meetups", 
                                                        data = json.dumps(self.meetup_incorrect), 
                                                        content_type="application/json")                                             
        self.assertEqual(response.status_code, 400)

    def test_invalid_datetime(self):
        '''test where the date is invalid'''
        response = self.client.post("/api/v1/meetups", 
                                                        data = json.dumps(self.meetup_invalid_date), 
                                                        content_type="application/json")                                             
        self.assertEqual(response.status_code, 400)

    def test_not_string(self):
        '''test where one of the fields that should be a string  is given in form of an integer'''
        response = self.client.post("/api/v1/meetups", 
                                                        data = json.dumps(self.meetup_not_string), 
                                                        content_type="application/json")                                             
        self.assertEqual(response.status_code, 400)



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

    def tearDown(self):
        self.app = None

         

