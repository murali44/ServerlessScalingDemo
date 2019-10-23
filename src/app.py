import boto3
import json
import os

# *********** Utils ***********

def add_cors_headers(response):
    response['headers'] = {'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*'}
    return response


# *********** APIs ************

def handler(event, context):
    print(event)
    name = os.environ['NAME']
    print(name)

    message = 'Hello ' + name + '!'
    item = {
        'message' : message
    }

    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(item)
    }

    return add_cors_headers(response)
