##### Make Exceptions ######
class NotInRange(Exception):
    'Raised when euler problem input is not in range of completed problems'

class NotYesNo(Exception):
    'Raised when answer to continue is not y or n'