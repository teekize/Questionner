from flask import Flask
from app.api.v1.meetups.views.views import meetups
from app.api.v1.question.views.question_views import question_blueprint
from app.api.v1.rsvp.views.rsvp_views import rsvp_blueprint


def createapp():
    app=Flask(__name__)

    app.register_blueprint(meetups)
    app.register_blueprint(question_blueprint)
    app.register_blueprint(rsvp_blueprint)

    
    return app