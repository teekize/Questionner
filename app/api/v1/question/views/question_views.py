from flask import Blueprint, jsonify, request
from app.api.v1.question.models import question_model#MeetUp, meetups
import datetime

question_blueprint=Blueprint("question_blueprint", __name__)

@question_blueprint.route("/questions", methods=["POST"])
def post_question():
    if not request.json or not "body" in request.json:
        return jsonify({"status":400,
                        "message":"Required fields missing"
            })
    body = request.json["body"]
    asked_by = request.json["createdBy"]
    title = request.json["title"]
    meetup = request.json["meetup"]

    if question_model.Question_Validators.validate_post(body, asked_by, title) != True:
        return jsonify({"status": 400,
                        "error" : "invalid data"
                        })
    else:

        new_question={
            "id" : question_model.questions[-1]["id"]+1,
            "createdOn" : datetime.datetime.utcnow(),
            "createdBy" : asked_by,
            "body" : body,
            "title" : title,
            "meetup" : meetup,
            "votes" : 0
        }

        question_model.questions.append(new_question)
        return jsonify(
            {"status":201,
            "data":[
                {"user": new_question["createdBy"],
                 "title" : new_question["title"],
                 "body" : new_question["body"],
                 "meetup" : new_question["meetup"]
                }
            ]
            }
        )

@question_blueprint.route("/questions/<int:question_id>/upvote", methods=["PATCH"])
def upvote_question(question_id):
    requested_question=[question for question in question_model.questions if question["id"]== question_id]
    if len(requested_question) == 0:
        return jsonify({"status": 404,
                        "error" : "Resource not found"
                        })

    else:
        requested_question[0]["votes"] = requested_question[0]["votes"]+1
        return jsonify(
            {"status": 201,
             "data" : [
                 {"meetup": requested_question[0]["meetup"],
                 "title" : requested_question[0]["title"],
                 "body" : requested_question[0]["body"],
                 "votes" : requested_question[0]["votes"]}
             ]
            }
        )
