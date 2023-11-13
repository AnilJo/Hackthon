import boto3
import os
import time

# Set up AWS credentials (consider using environment variables for better security)
AWS_ACCESS_KEY_ID="##########"
AWS_SECRET_ACCESS_KEY="###############"
AWS_DEFAULT_REGION="us-east-1"

# Initialize a boto3 CloudFormation client
cf_client = boto3.client(
    'cloudformation',
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_DEFAULT_REGION
    )

# Specify the template file (assuming it is in the same directory as this script)
template_body = open('cur_setup.yaml', 'r').read()

# Specify the stack name
stack_name = "CURSetupStack"

# Specify the parameters
parameters = [
    {
        'ParameterKey': 'BucketPrefix',
        'ParameterValue': 'mybucket12375'  # Replace with your desired prefix
    }
]

try:
    print(f"Creating stack {stack_name}...")
    response = cf_client.create_stack(
        StackName=stack_name,
        TemplateBody=template_body,
        Parameters=parameters,
        Capabilities=[
            'CAPABILITY_IAM',  # Add this if your CF template includes IAM resources
            'CAPABILITY_NAMED_IAM',
        ]
    )
    print(f"Stack creation initiated, response: {response}")
except cf_client.exceptions.ClientError as e:
    print(f"Failed to create stack: {e}")
