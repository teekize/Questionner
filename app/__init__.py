from flask import Flask
from app.api.v1.meetups.views.views import meetups as meetup_blueprint

def createapp():
    app=Flask(__name__)
    app.register_blueprint(meetup_blueprint)
    return app