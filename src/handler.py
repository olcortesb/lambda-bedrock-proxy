import json
from src.client_bedrock import titan_model 

def hello(event, context):

    question = "how to calculate the factorial of a number"
    text = titan_model(question)
    response = {"statusCode": 200, "body": json.dumps(text)}

    return response