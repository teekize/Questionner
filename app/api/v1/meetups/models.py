import datetime
meetupdb = []

class MeetUpModel:
    """contains all methods required for the Meetup endpoints"""
    
    def __init__(self):
        self.day_ = datetime.datetime.utcnow().strftime('%Y-%M-%d  %I : %M %S %p')
        self.db = meetupdb
        self.id = len(meetupdb) +1

    
    def check_in_db(self, _id):
        data_in_db = [meetup for meetup in self.db if meetup["id"] == _id]
        if len(self.db) != 0:
            return data_in_db
        return None

    def save(self, topic, happeningOn, name, location, tag, image):

        new_meetup = {
            "id" : len(self.db) +1, 
            "createdOn" : self.day_,
            "location": location,
            "topic": topic,
            "happeningOn": happeningOn,
            "tag": tag,
            "image" : image
        }
        meetupdb.append(new_meetup)
        return {"status_code": 201, 
                        "data" : [
                                    {
                                        "id" : new_meetup["id"], 
                                        "location": new_meetup["location"],
                                        "topic": new_meetup["topic"],
                                        "happeningOn": new_meetup["happeningOn"],
                                        "tag": new_meetup["tag"],
                                        "image" : new_meetup["image"]
                                    }
                                ]
                       }
    
    def get_all_upcoming(self):
        results = [meetup for meetup in self.db if meetup["happeningOn"] > datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M')]
        if not results:
            return {"error" : "no  upcoming meetups", "satus" : 404}
        return {"data" : results}

    
    def get_one(self, _id):
        results = self.check_in_db( _id)
        if not results :
            return {"status" : 404, 
                    "error" : "Meetup not found"}

        return {"status": 200,
                "data": [
                            {"id": results[0]["id"], 
                            "topic": results[0]["topic"], 
                            "location": results[0]["location"], 
                            "tag": results[0]["topic"]
                            }
                        ]
        }