from flask import Flask


def createapp():
    app=Flask(__name__)
    from app.api.v1.meetups.views.views import meetups
    app.register_blueprint(meetups)
    return app