import os
import sys
file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)

from utils import create_policy as cp
from utils import decode_token as auth

def handle(event, context):
    principal_id = 'user_stage'
    try:
        headerAuth = event['authorizationToken']  # retrieve the Auth token
        token = headerAuth.split(' ')[1]
        print('token authorizationToken', headerAuth, token)
        policy = cp.create_policy(event['methodArn'], principal_id)

        if event['authorizationToken']:
            user_info = auth.auth_token_decode(token)
            if user_info:
                policy.allowAllMethods()
            else:
                policy.denyAllMethods()
        else:
            policy.denyAllMethods()

        return policy.build()
    except Exception as e:
        print("error", e)
        policy = cp.create_policy(event['methodArn'], principal_id)
        policy.denyAllMethods() 
        return policy.build()



if __name__ == "__main__":
    handle({}, '')