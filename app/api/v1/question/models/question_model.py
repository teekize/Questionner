questions=[
    {
        "id" : 1,#Integer,
        "createdOn" : "2019, 10, 1",#Date,
        "createdBy" : 1,#Integer, // represents the user asking the question
        "meetup" : 1,#Integer, // represents the meetup the question is for
        "title" : "money",#String,
        "body" : "why is the greece economy still struglling",#String,
        "votes" : 2#Integer,
    },

    {
        "id" : 2,#Integer,
        "createdOn" : "2019, 11, 1",#Date,
        "createdBy" : 2,#Integer, // represents the user asking the question
        "meetup" : 3,#Integer, // represents the meetup the question is for
        "title" : "health",#String,
        "body" : "did you know malaria is the eading killer in kenay",#String,
        "votes" : 3#Integer,
    }
]


class Question_Validators:
    # def __init__(self, createdOn, id):
    #     self.createdOn=datetime.datetime.utcnow()
    #     self.id=len(meetup)+1
    #     # self.CreatedBy=S
    # self.check_string=
   
   @staticmethod
   def validate_post(title, body, createdBy):
       if type(title) != str:
           return False
    #    return True

       if type(body) != str:
           return False
    #    return True

       if type(createdBy) != int:
           return False
    #    return True
        
       else:
           return True
    #    else:
    #        return True

    # #    if type(happeningOn) != str:
    # #        return False
    # #    return True
        