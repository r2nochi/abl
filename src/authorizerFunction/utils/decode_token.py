import os
import jwt

def auth_token_decode(auth_token):
    """
    Checks whether JWT Token is valid or not.
    If valid returns True else False
    """
    try:
        isValid = jwt.decode(auth_token, os.environ['SECRET_KEY'], algorithms=["HS256"])
        print('isValid', isValid)
        return True
    except jwt.ExpiredSignatureError:
        print("Token is expired")
        return False
    except jwt.InvalidSignatureError:
        print("Token has invalid sign")
        return False
    except jwt.InvalidTokenError:
        print("Invalid token")
        return False
    except Exception as e:
        print("error", e)
        return False

if __name__ == "__main__":
    auth_token_decode('eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6Ik5vbmUiLCJ1c2VybmFtZSI6ImRldiIsInBhc3N3b3JkIjoiZGV2LioiLCJleHAiOjE2Mjk5MzY0OTR9.vuzfYiiXKi65B1Zv-IemVn_-QWLjQptflg-N1NFRLYk')