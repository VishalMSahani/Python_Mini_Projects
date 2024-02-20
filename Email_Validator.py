import re

def Email_Validator(email):
    patter = r'^[a-zA-Z0-9._%+-]+@gmail\.com$'
    if re.match(pattern,email):
