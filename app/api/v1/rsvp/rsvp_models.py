from app.api.v1.meetups.models import meetupdb
from app.api.v1.question.question_model import QuestionModel

rsvp_db = []

class RsvpModel(QuestionModel):
    def save(self, _id, response, user):
        requested_meetup = [meetup for meetup in self.db if meetup["id"] == _id]
        if not requested_meetup:
            return {"status" : 404,
                    "message" : "that meetup is not existent"
                    }
        if type(response) != str:
            return {"status" : 400 , "error" : "your response should be string only"}

        _check_given_response = response.lower()
        if _check_given_response not in ("yes", "no", "maybe"):
            return {"status" : 400, "error" : "your seponse can only be yes, no or maybe"}
        
        new_rsvp = {
                    "id" : len(rsvp_db) +1,
                    "meetup" : requested_meetup[0]["id"],
                    "user" : user,
                    "response" : response
                   }
        rsvp_db.append(new_rsvp)
        
        return {"status" : 201,
                "data" : [
                          {
                            "meetup" : new_rsvp["id"],
                            "topic" : requested_meetup[0]["topic"],
                            "status" : new_rsvp["response"]
                          }
                         ]
                }



