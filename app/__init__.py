from flask import Flask
from app.api.v1.meetups.meetups_views import meetups
from app.api.v1.question.question_views import question_blueprint
from app.api.v1.rsvp.rsvp_views import rsvp_blueprint


def createapp():
    app=Flask(__name__)

    app.register_blueprint(meetups)
    app.register_blueprint(question_blueprint)
    app.register_blueprint(rsvp_blueprint)

    
    return app