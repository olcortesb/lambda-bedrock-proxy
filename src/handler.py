import json
from src.client_bedrock import titan_model 

def hello(event, context):
    q = json.loads(event['body'])
    text = titan_model(json.dumps(q['question']))
    response = {"statusCode": 200, "body": json.dumps(text)}

    return response