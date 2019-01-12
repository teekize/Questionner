from flask import Blueprint, jsonify, request
from app.api.v1.meetups.models import meetup #MeetUp, meetups
import datetime

meetups=Blueprint("meetups", __name__, url_prefix = "/api/v1") #)

@meetups.route("/meetups", methods=["POST"])
def create_meetup():
    if not request.json or not "topic" in request.json:
        return jsonify({"message":"Required fields missing"}), 204

    name = request.json.get("name")
    location = request.json.get("location")
    topic = request.json.get("topic")
    tags = request.json["tags"]
    images = request.json["images"]
    happeningOn=request.json["happeningOn"]

    if meetup.MeetUp.validate_post(images, location, name, topic, tags)!=True:
        return jsonify({"message":"Invalid inputs"}), 404
        
    else:
        new_meetup={
            "id" : meetup.meet_ups[0]["id"] +1,
            "createdOn" : datetime.datetime.utcnow(),
            "name" : name,
            "location" : location,
            "topic" : topic,
            "tags" : tags,
            "images" : images,
            "happeningOn" : happeningOn
        }

        meetup.meet_ups.append(new_meetup)
        return jsonify({"status_code": 201, 
                        "data" : [
                                 {"id" :new_meetup["id"], 
                                "location":new_meetup["location"],
                                "topic": new_meetup["topic"],
                                "happeningOn": new_meetup["happeningOn"],
                                "tags": new_meetup["tags"],
                                "images" : new_meetup["images"]
                                 }
                                ]

                       }
                        ) ,201

@meetups.route("/meetups/<int:meetup_id>", methods=["GET"])
def get_one_meetup(meetup_id):
    meetup_requested=[meetup for meetup in meetup.meet_ups if meetup["id"]==meetup_id]
    return jsonify(
        {"status":200,
        "data": [
                {"id":meetup_requested[0]["id"], 
                "topic":meetup_requested[0]["topic"], 
                "location":meetup_requested[0]["location"], 
                "tag":meetup_requested[0]["topic"]
                }
                ]
        }
    )
    

@meetups.route("/meetups/upcoming", methods=["GET"])
def get_all_meetup():
    meetup_requested=[meetup for meetup in meetup.meet_ups ]
    return jsonify(
        {"status":200,
        "data": [
                meetup_requested[0:]
                ]
        }
    )
    
    #     



        #name, location, topic, tags, images