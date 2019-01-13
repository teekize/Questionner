# questions=[
#     {
#         "id" : 1,#Integer,
#         "createdOn" : "2019, 10, 1",#Date,
#         "createdBy" : 1,#Integer, // represents the user asking the question
#         "meetup" : 1,#Integer, // represents the meetup the question is for
#         "title" : "money",#String,
#         "body" : "why is the greece economy still struglling",#String,
#         "votes" : 2#Integer,
#     },

#     {
#         "id" : 2,#Integer,
#         "createdOn" : "2019, 11, 1",#Date,
#         "createdBy" : 2,#Integer, // represents the user asking the question
#         "meetup" : 3,#Integer, // represents the meetup the question is for
#         "title" : "health",#String,
#         "body" : "did you know malaria is the eading killer in kenay",#String,
#         "votes" : 3#Integer,
#     }
# ]


# class Question_Validators:
#     # def __init__(self, createdOn, id):
#     #     self.createdOn=datetime.datetime.utcnow()
#     #     self.id=len(meetup)+1
#     #     # self.CreatedBy=S
#     # self.check_string=
   
#    @staticmethod
#    def validate_post(title, body, createdBy):
#        if type(title) != str:
#            return False
#     #    return True

#        if type(body) != str:
#            return False
#     #    return True

#        if type(createdBy) != str:
#            return False
#     #    return True
        
#        else:
#            return True
#     #    else:
#     #        return True

#     # #    if type(happeningOn) != str:
#     # #        return False
#     # #    return True
    
import datetime
from app.api.v1.meetups.models import MeetUpModel
questiondb =[]

class QuestionModel(MeetUpModel):
    def __init__(self):
        self.db = questiondb
        self.vote = 0
        self.createdOn = datetime.datetime.utcnow().strftime('%Y-%M-%d  %I : %M %S %p')
        super().__init__()
        
    
    def save(self, createdBy, meetup, title, body):
        
        # response = self.check_in_db()
        new_question = {
            "question_id" : self.id,
            "createdBy" : createdBy,
            "createdOn" : self.day_,
            "meetup" : meetup,
            "title" : title,
            "body" : body,
            "vote" : self.vote
        }

        self.db.append(new_question)
        return {"status" : 201,
                "data" : [
                          {
                            "question_id" : new_question["question_id"],
                            "createdOn" : self.createdOn,
                            "createdBy" : new_question["createdBy"],
                            "body" : new_question["body"],
                            "title" : new_question["title"],
                            "meetup" : new_question["meetup"]
                          }
                ]
        }

    def upvote_downvote_question(self, question_id, _num):
        result = [question for question in self.db if question["question_id"] == question_id]
        if not result:
            return {"status" : 404,
                    "error" : "question with the id not found"
                   }
        else:
            if _num == 0:
                result[0]["vote"] = result[0]["vote"] +1
            if _num == 1:
                result[0]["vote"] = result[0]["vote"] -1
            return {
                    "status" :200,
                    "data" : [{
                                "meetup": result[0]["meetup"],
                                "title" : result[0]["title"],
                                "body" : result[0]["body"],
                                "vote" : result[0]["vote"]
                                }
                                ]
                    }
