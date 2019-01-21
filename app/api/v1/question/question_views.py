from flask import Blueprint, jsonify, request
from app.api.v1.question.question_model import QuestionModel
from app.api.v1.validation import ValidationModule
import datetime

question_blueprint=Blueprint("question_blueprint", __name__, url_prefix= "/api/v1")
question = QuestionModel()
validator = ValidationModule()


    

@question_blueprint.route("/questions", methods=["POST"])
def post_question():
    incoming_request = request.json
    required_fields = "body" , "createdBy", "title", "meetup"

    for field in required_fields:
        if field not in incoming_request or not incoming_request:
            return jsonify({
                            "status":400,
                            "message":"Required field ({}) missing".format(field)
                }), 400

    body = request.json["body"]
    createdBy = request.json["createdBy"]
    title = request.json["title"]
    meetup = request.json["meetup"]

    details = body, createdBy, title

    if validator.check_if_string(details) == False:
        return jsonify({"status": 400,
                        "error" : "input details need to be in the form of strings"
                        }), 400
    if validator.check_if_data_not_in_(details) == False:
        return jsonify({"status": 400,
                        "error" : "input details cannot be empty"
                        }), 400

    results = question.save(createdBy, meetup,title, body)
    return jsonify(results), 201

@question_blueprint.route("/questions/<int:question_id>/upvote", methods=["PATCH"])
def upvote_question(question_id):
    num = 0
    results = question.upvote_downvote_question(question_id, num)
    if 404 in results:
        return jsonify(results),404
    return jsonify (results), 201


@question_blueprint.route("/questions/<int:question_id>/downvote", methods=["PATCH"])
def downvote_question(question_id):
    num = 1
    results = question.upvote_downvote_question(question_id, num)
    if 404 in results:
        return jsonify(results),404
    return jsonify (results), 201