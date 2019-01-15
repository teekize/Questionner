from flask import Blueprint, jsonify, request
from app.api.v1.meetups.models  import MeetUpModel
import datetime
import re

meetups = Blueprint("meetups", __name__, url_prefix = "/api/v1")
model = MeetUpModel()

"""
Adds validators to the requests that the user is passing
The required fields for the create meetup endpoint are :
name of meetup, location , topic, tag, image, happeningOn
If these miss then the an error message should be outputed
stating that its missing a required field

"""

def Validator(details, date):
    for value in details:
        if type(value) != str:
            return False
        
    
    for input_ in details:
        if len(input_) == 0:
            return False
    try:
        datetime.datetime.strptime(date, '%Y-%m-%d %H:%M')
    except ValueError:
        return False
    
    
@meetups.route("/meetups", methods=["POST"])
def create_meetup():
    payload = request.json
    required = "name", "location", "topic", "tag", "image" , "happeningOn"

    for field in required:  
        if field not in payload :
            return jsonify({"error" : "Bad request"}), 400

    name = request.json.get("name")
    location = request.json.get("location")
    topic = request.json.get("topic")
    tag = request.json.get("tag",)
    image = request.json.get("image",)
    happeningOn=request.json.get("happeningOn")

    details = name, location, topic, tag, image, happeningOn
    date = happeningOn

    if Validator(details, date) == False:
        return jsonify({"error": "check your meetup details "}),404
    response = model.save(topic, happeningOn, name, location, tag, image)
    return jsonify(response), 201

@meetups.route("/meetups/<int:meetup_id>", methods=["GET"])
def get_one_meetup(meetup_id):
    result = model.get_one(meetup_id)
    if 404 in result:
        return jsonify(result), 404
    return jsonify(result), 200
    

@meetups.route("/meetups/upcoming", methods=["GET"])
def get_all_meetup():
    results = model.get_all_upcoming()
    if 404 in results:
        return jsonify(results), 404 
    return jsonify(results), 200
    