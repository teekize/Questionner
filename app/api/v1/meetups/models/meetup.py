import datetime

meetups=[
    {
        "id":1,
        "createdOn" : datetime.datetime.utcnow(),#Date,
        "location" : "Nairobi",#String,
        "images" : "pintrest.png",#[String, String], // OPTIONAL: URL to the image location
        "topic" : "effect of global warming",#String,
        "happeningOn" : datetime.date(2019,1,10),#Date, // when the meetup is holding
        "Tags" : "climate"#[String, String, ....]
        # "CreatedBy":"""
    },

    {
        "id":2,
        "createdOn" : datetime.datetime.utcnow(),#Date,
        "location" : "Mombasa",#String,
        "images" : "pintrest.png",#[String, String], // OPTIONAL: URL to the image location
        "topic" : "Asthma attacks",#String,
        "happeningOn" : datetime.date(2019,1,11),#Date, // when the meetup is holding
        "Tags" : "health"#[String, String, ....]
        # "CreatedBy":""
    }
]

# class MeetUp:
#     # def __init__(self, createdOn, id):
#     #     self.createdOn=datetime.datetime.utcnow()
#     #     self.id=len(meetup)+1
#     #     # self.CreatedBy=S

#     def create(self):
#         meetups.append()

        