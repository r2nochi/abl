from .auth_policy import AuthPolicy

def create_policy(method_arn, principal_id):
    tmp = method_arn.split(':')
    region = tmp[3]
    account_id = tmp[4]
    api_id, stage = tmp[5].split('/')[:2]

    policy = AuthPolicy(principal_id, account_id)
    policy.restApiId = api_id
    policy.region = region
    policy.stage = stage
    return policy