import datetime

day=datetime.date(2019, 1, 10)

meet_ups=[
    {
        "id":1,
        "createdOn" : "2019, 1, 10",#Date,
        "location" : "Nairobi",#String,
        "images" : "pintrest.png",#[String, String], // OPTIONAL: URL to the image location
        "topic" : "effect of global warming",#String,
        "happeningOn" : '2019, 1, 10',#Date, // when the meetup is holding
        "Tags" : "climate"#[String, String, ....]
        # "CreatedBy":"""
    },

    {
        "id":2,
        "createdOn" : "2019, 1, 10",#Date,
        "location" : "Mombasa",#String,
        "images" : "pintrest.png",#[String, String], // OPTIONAL: URL to the image location
        "topic" : "Asthma attacks",#String,
        "happeningOn" : '2019, 1, 10',#Date, // when the meetup is holding
        "Tags" : "health"#[String, String, ....]
        # "CreatedBy":""
    }
]

class MeetUp:
    # def __init__(self, createdOn, id):
    #     self.createdOn=datetime.datetime.utcnow()
    #     self.id=len(meetup)+1
    #     # self.CreatedBy=S
    # self.check_string=
   
   @staticmethod
   def validate_post(images, location, name, topic, tags):
       if type(topic) != str:
           return False
    #    return True

       if type(location) != str:
           return False
    #    return True

       if type(name) != str:
           return False
    #    return True
        

       if type(images) != str:
           return False
    #    return True

       if type(tags) != str:
           return False
    #    return True
       else:
           return True

    #    if type(happeningOn) != str:
    #        return False
    #    return True
        