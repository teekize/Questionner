from flask import Blueprint, jsonify, request
from app.api.v1.meetups.models import meetup #MeetUp, meetups
import datetime

meetups=Blueprint("__name__", "meetup_blueprint")

@meetups.route("/meetups", methods=["POST"])
def create_meetup():
    if not request.json or not "topic" in request.json:
        return jsonify({"message":"Required fields missing"})
    
    if not "happeningOn" in request.json or not "location" in request.json:
        return jsonify({"message":"required fileds missing"}) 

    name = request.json["title"]
    location = request.json["location"]
    topic = request.json["topic"]
    tags = request.json["tags"]
    images = request.json["images"]

    if meetup.MeetUp.validate_post(images, location, name, topic, tags)==True:
        new_meetup={
            "id" : meetup.meet_ups[0]["id"] +1,
            "createdOn" : datetime.datetime.utcnow(),
            "name" : name,
            "location" : location,
            "topic" : topic,
            "tags" : tags,
            "images" : images,
        }

        meetup.meet_ups.append(new_meetup)
        return jsonify({"message" : [{"id" :new_meetup["id"]}]}), 201


        #name, location, topic, tags, images