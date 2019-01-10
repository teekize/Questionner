from flask import Blueprint, jsonify, request
from app.api.v1.meetups.models import meetup #MeetUp, meetups
import datetime

meetups=Blueprint("meetups", __name__) #)

@meetups.route("/meetups", methods=["POST"])
def create_meetup():
    if not request.json or not "topic" in request.json:
        return jsonify({"message":"Required fields missing"})
    
    # if not "happeningOn" in request.json or not "location" in request.json:
    #     return jsonify({"message":"required fileds missing"}) 

    name = request.json["name"]
    location = request.json["location"]
    topic = request.json["topic"]
    tags = request.json["Tags"]
    images = request.json["images"]

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
        }

        meetup.meet_ups.append(new_meetup)
        return jsonify({"status_code":201, 
                        "data" : [{"id" :new_meetup["id"], "location":new_meetup["location"]}
                                 
                                 ]

                       }
                        )


        #name, location, topic, tags, images