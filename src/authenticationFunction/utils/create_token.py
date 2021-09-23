import jwt 
import datetime
import os


def create_access_token(result):
    # Returns new JWT Token.
    jwt_info = jwt.encode({
        "id": str(result.get('id')),
        "username": result.get('username'),
        "status": result.get('status'),
        "organization": result.get('organization'),
        "exp": datetime.datetime.utcnow() + datetime.timedelta(seconds=28800)
        },
        os.environ['SECRET_KEY'],
        algorithm="HS256"
    )
    print('jwt_info', jwt_info)
    return jwt_info


if __name__ == "__main__":
    create_access_token({
        'first_name': 'mockuser',
        'last_name': 'mockpassword',
        id: '1'
    })