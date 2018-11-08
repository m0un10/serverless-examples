import boto3
import json
import argparse

class test_context(dict):
    '''This is a context for running tests locally'''
    def __init__(self,profile,region):
        self.profile = profile
        self.region = region

def lambda_handler(event, context):

    data = json.loads(event['body'])

    if 'stack-name' in data:
        stack_name = data['stack-name']
    else:
        print "failing due to invalid inputs"
        return {
            "statusCode": 500,
            "body": "stack-name must be set"
        }
        return response

    print "Destroy stack " + stack_name

    # For local testing
    if isinstance(context,test_context):
        print "Profile: " + context.profile
        print "Region: " + context.region
        session = boto3.session.Session(profile_name=context.profile,region_name=context.region)
    # When called by Lambda
    else:
        session = boto3.session.Session()

    result = session.client('cloudformation').delete_stack(
        StackName=stack_name
    )
    print result

    response = {
        "statusCode": 200
    }
    return response

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Lambda Function to destroy cloudformation stack.')
    parser.add_argument("-r","--region", help="Region in which to run.", default='us-east-1')
    parser.add_argument("-p","--profile", help="Profile name to use when connecting to aws.", default='personal')
    parser.add_argument("-n","--name", help="Name of the stack")
    args = parser.parse_args()
    event =  {
        'body': json.dumps({
            'stack-name': args.name
        })
    }
    context = test_context(args.profile,args.region)
    lambda_handler(event, context)
