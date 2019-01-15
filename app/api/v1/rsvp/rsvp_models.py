from app.api.v1.meetups.models import meetupdb
from app.api.v1.question.question_model import QuestionModel

rsvp_db = []

class RsvpModel(QuestionModel):
    def save(self, _id, response, user):
        requested_meetup = [meetup for meetup in meetupdb if meetup["id"] == _id]
        if not requested_meetup:
            return {"status" : 403,
                    "message" : "that meetup is not existent"
                    }

        new_rsvp = {
                    "id" : len(rsvp_db) +1,
                    "meetup" : requested_meetup[0]["id"],
                    "user" : user,
                    "response" : response
                   }
        rsvp_db.append(_id, response, user)
        
        return {"status" : 201,
                "data" : [
                          {
                            "meetup" : new_rsvp["id"],
                            "topic" : requested_meetup[0]["topic"],
                            "status" : new_rsvp["response"]
                          }
                         ]
                }



