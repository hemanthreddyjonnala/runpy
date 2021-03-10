
#System Manager:
#Experienced in storing configuration and secrets using AWS System Manager and access them using boto3 client

import boto3
import pprint

client = boto3.client('ssm')

def handler(event, context):
    param_name = 'REPLACE_ME'
    response = client.get_parameter(Name=param_name)
    
    pprint.PrettyPrinter().pprint(response['Parameter'])

    return response['Parameter']['Value']

