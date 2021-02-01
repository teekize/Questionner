import string
import datetime
class ValidationModule:
    """contains the validtors for the endpoints"""

    def check_if_string(self, data):
        for value in data:
            if type(value) != str:
                return False

    def check_not_empty(self,data):
        for value in data:
            if len(value) == 0:
                return False
    
    
    def check_if_data_not_in_(self, data):
        for input_ in data.values():
            string_to_strip = input_.strip()
            if len(string_to_strip) <= 3:
                return False
            
    def check_date_if_matches(self, data):
        date = data.get("happeningOn")
        
        try:
            datetime.datetime.strptime(date, '%Y-%m-%d %H:%M')
        except ValueError:
            return False

   