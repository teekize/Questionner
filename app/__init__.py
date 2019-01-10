from flask import Flask


def createapp():
    app=Flask(__name__)

    from app.api.v1.meetups.views.views import meetups
    from app.api.v1.question.views.question_views import question_blueprint

    app.register_blueprint(meetups)
    app.register_blueprint(question_blueprint)
    
    return app