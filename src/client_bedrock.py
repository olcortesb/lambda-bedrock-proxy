import boto3
import botocore
import json

bedrock_runtime = boto3.client('bedrock-runtime', region_name='us-east-1')

def titan_model(prompt):
    
    body = json.dumps({
        "inputText": prompt, 
        "textGenerationConfig":{
            "maxTokenCount":4096,
            "stopSequences":[],
            "temperature":0,
            
            "topP":0.9
            }
        })
    
    print(body)

    modelId = 'amazon.titan-text-express-v1' # change this to use a different version from the model provider
    accept = 'application/json'
    contentType = 'application/json'
    outputText = "\n"
    
    text = bedrock_runtime.invoke_model(body=body, modelId=modelId, accept=accept, contentType=contentType)
    response_body = json.loads(text.get('body').read())
    
    outputText = response_body.get('results')[0].get('outputText')
    #return outputText

    response = {"statusCode": 200, "body": json.dumps(outputText)}

    return response

def llama_model(prompt):

    body = json.dumps({ 
    	'prompt': prompt,
        'max_gen_len': 512,
    	'top_p': 0.9,
    	'temperature': 0.2
    })

    modelId = 'meta.llama2-70b-chat-v1' # change this to use a different version from the model provider
    accept = 'application/json'
    contentType = 'application/json'
    outputText = "\n"

    response = bedrock_runtime.invoke_model(body=body, modelId=modelId, accept=accept, contentType=contentType)
    response_body = json.loads(response.get('body').read().decode('utf-8'))

    outputText = response_body['generation'].strip()

    response = {"statusCode": 200, "body": json.dumps(outputText)}

    return response