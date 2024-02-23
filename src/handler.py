import json
from src.client_bedrock import titan_model, llama_model

from enum import Enum

class Model(Enum):
    TITAN = 'titan'
    LLAMA = 'llama'
    NONE = 'none'

    @classmethod
    def _missing_(cls, value):
        return cls.NONE

def hello(event, context):

    q = json.loads(event['body'])
    model = Model(q['model'])
    
    match model:
        case Model.TITAN:
            text = titan_model(json.dumps(q['question']))
        case Model.LLAMA:
            text = llama_model(json.dumps(q['question']))
        case Model.NONE:
            text = "Model does not match"

    response = {"statusCode": 200, "body": json.dumps(text)}

    return response