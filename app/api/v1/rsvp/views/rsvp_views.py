from flask import Blueprint, jsonify, request
from app.api.v1.rsvp.models import rsvp_models
from app.api.v1.meetups.models import meetup 
import datetime

rsvp_blueprint=Blueprint("rsvp_blueprint", __name__, url_prefix= "/api/v1")

@rsvp_blueprint.route("/meetups/<int:meetup_id>/rsvp", methods=["POST"])
def post_rsvp(meetup_id):
    requested_meetup =[meetup for meetup in meetup.meet_ups if meetup["id"] == meetup_id ]
    if len(requested_meetup) == 0:
        return jsonify({"status":400,
                        "message":"Required fields missing"
            })
    if not request.json or not "response" in request.json:
        return jsonify({"status":400,
                        "message":"Required fields missing"
            })
    response =request.json["response"]
    if rsvp_models.Rsvp_Validators.validate_post(response) != True:
        return jsonify({"status":400,
                        "message":"Required fields missing"
            })

    else:
        new_rsvp ={
            "id" : len(rsvp_models.rsvp_models) +1,
            "meetup" : requested_meetup[0]["id"],
            "user" : request.json["user"],
            "response" : response
        }

        rsvp_models.rsvp_models.append(new_rsvp)
        return jsonify({"status":201, 
                        "data" : [
                                 {
                                   "meetup" : new_rsvp["id"],
                                   "topic" : requested_meetup[0]["topic"],
                                   "status" : new_rsvp["response"]
                                 }
                                ]
                       }
                        ), 201