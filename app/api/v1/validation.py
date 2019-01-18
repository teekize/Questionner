import string
import datetime
class ValidationModule:
    """contains the validtors for the endpoints"""

    def check_if_string(self, data):
        for value in data:
            if type(value) != str:
                return False
    
    
    def check_if_data_not_in_(self, data):
        for input_ in data:
            if len(input_) == 0:
                return False
            
    def check_date_if_matches(self, date):
        try:
            datetime.datetime.strptime(date, '%Y-%m-%d %H:%M')
        except ValueError:
            return False

    def check_if_data_is_whitespace(self, data):
        for input_ in data:
            if input_.isspace() == True:
                return False