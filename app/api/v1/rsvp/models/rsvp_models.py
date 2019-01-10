rsvp_models=[
    {
        "id": 1,
        "meet_up" : 1,
        "user" : 1,
        "response" : "yes"
    },

    {
        "id": 2,
        "meet_up" : 2,
        "user" : 2,
        "response" : "no"
    }
]

class Rsvp_Validators:
   '''this class contains the validators for the rsvp endpoint'''
   @staticmethod
   def validate_post(response):
       if type(response) != str:
           return False
       else:
           return True    
        