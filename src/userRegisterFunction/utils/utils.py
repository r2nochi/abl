import re
import json
import smtplib 
from random import randint

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
def email_validator(email):
    if re.fullmatch(regex, email) and email:
        return True
    else:
        return False

def pw_validator(password, lon):
    if len(password) >= lon and password:
        return True
    else:
        return False


def random_number(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

def construct_error(statusCode, mssg):

    return dict(statusCode = statusCode, body = json.dumps({
            "status": "FAILED",
            "message": mssg
        }))

