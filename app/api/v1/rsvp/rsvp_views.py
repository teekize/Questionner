from flask import Blueprint, jsonify, request
from app.api.v1.rsvp.rsvp_models import meetupdb, RsvpModel
from app.api.v1.meetups import models 
import datetime

instance_rsvp = RsvpModel()
rsvp_blueprint=Blueprint("rsvp_blueprint", __name__, url_prefix= "/api/v1")

@rsvp_blueprint.route("/meetups/<int:meetup_id>/rsvp", methods=["POST"])
def post_rsvp(meetup_id):
    incoming_request = request.json
    required_fields = "response", "meetupid", "user"
    for field in required_fields:
        if field not in incoming_request or not incoming_request:
            return jsonify({
                            "status":403,
                            "message":"Required fields missing"
                }), 403
    response_from_user =request.json["response"]
    user_to_rsvp = request.json["user"]
    meetup_id_to_rsvp = request.json["id"]

    result_from_save = instance_rsvp.save(meetup_id_to_rsvp, response_from_user, user_to_rsvp)

    if not 404 in result_from_save:
        return jsonify(result_from_save), 201
    return jsonify(result_from_save), 404

    
    
    
