import boto3
import json
import argparse

class test_context(dict):
    '''This is a context for running tests locally'''
    def __init__(self,profile,region):
        self.profile = profile
        self.region = region

def lambda_handler(event, context):
    
    stack_name = "default"
    key_name = "default"
    instance_type = "t2.micro"

    data = json.loads(event['body'])

    if 'stack-name' in data:
        stack_name = data['stack-name']
    if 'key-name' in data:
        key_name = data['key-name']

    if not 'db-credential' in data:
        return {
            "statusCode": 500,
            "body": "db-credential must be set"
        }
        return response

    db_credential = data['db-credential']
    print "Creating stack " + stack_name + " and using key " + key_name

    # For local testing
    if isinstance(context,test_context):
        print "Profile: " + context.profile
        print "Region: " + context.region
        session = boto3.session.Session(profile_name=context.profile,region_name=context.region)
    else:
        session = boto3.session.Session()

    session.client('cloudformation').create_stack(
        StackName=stack_name,
        TemplateURL='https://s3.amazonaws.com/awsiammedia/public/sample/ManagingSecrets/secrets-s3-blog.template',
        TimeoutInMinutes=123,
        OnFailure='ROLLBACK',
        Tags=[
            {
                'Key': 'Name',
                'Value': stack_name
            }
        ],
        Parameters=[
            {
                'ParameterKey': 'DbPassword',
                'ParameterValue': db_credential
            },
            {
                'ParameterKey': 'InstanceType',
                'ParameterValue': 't2.micro'
            },
            {
                'ParameterKey': 'KeyName',
                'ParameterValue': key_name
            },
            {
                'ParameterKey': 'SourceCidr',
                'ParameterValue': '0.0.0.0/0'
            }
        ],
        Capabilities=[
            'CAPABILITY_IAM',
        ]
    )

    response = {
        "statusCode": 200
    }
    return response

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Lambda Function to create cloudformation stack.')
    parser.add_argument("-r","--region", help="Region in which to run.", default='us-east-1')
    parser.add_argument("-p","--profile", help="Profile name to use when connecting to aws.", default='personal')
    parser.add_argument("-n","--name", help="Name of the stack")
    parser.add_argument("-c","--credential", help="Password to be used for the stack")
    parser.add_argument("-k","--key", help="Key to be used")
    args = parser.parse_args()
    event =  {
        'body': json.dumps({
            'stack-name': args.name,
            'db-credential': args.credential,
            'key-name': args.key
        })
    }
    context = test_context(args.profile,args.region)
    lambda_handler(event, context)
