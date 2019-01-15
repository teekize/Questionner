import datetime
from app.api.v1.meetups.models import MeetUpModel
questiondb =[]

class QuestionModel(MeetUpModel):
    """ contains all methods to be used by Question endpoints"""
    def __init__(self):
        self.dbq = questiondb
        self.vote = 0
        self.ido = len(questiondb) +1
        self.createdOn = datetime.datetime.utcnow().strftime('%Y-%m-%d  %I : %M %S %p')
        super().__init__()
        
    
    def save(self, createdBy, meetup, title, body):
        new_question = {
                        "question_id" : self.ido,
                        "createdBy" : createdBy,
                        "createdOn" : self.createdOn,
                        "meetup" : meetup,
                        "title" : title,
                        "body" : body,
                        "vote" : self.vote
                        }

        self.dbq.append(new_question)
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
        result = [question for question in self.dbq if question["question_id"] == question_id]
        if not result:
            return {
                    "status" : 404,
                    "error" : "question with the id not found"
                   }
        else:
            if _num == 0:
                result[0]["vote"] = result[0]["vote"] +1

            if _num == 1 and result[0]["vote"] <= 0:
                result[0]["vote"] == 0
            elif _num == 1 and result[0]["vote"] <= 1:
                result[0]["vote"] = result[0]["vote"]-1
            return {
                    "status" :200,
                    "data" : [
                                {
                                    "meetup": result[0]["meetup"],
                                    "title" : result[0]["title"],
                                    "body" : result[0]["body"],
                                    "vote" : result[0]["vote"]
                                }
                             ]
                    }
