# lambda-bedrock-proxy
Handler AWS bedrock to diferente LLM

## Prerequisites

Python

```bash
python3.10 --version
# Python 3.10.12
```

Serverless framework

```bash
serverless --version
#Framework Core: 3.38.0
#Plugin: 7.2.0
#SDK: 4.5.1
```

AWS cli

```bash
aws --version
#aws-cli/1.32.48 Python/3.10.12 Linux/6.5.0-17-generic botocore/1.34.48
```

## Usage

- Download this repository
```
# by ssh for example
git clone git@github.com:olcortesb/serverless-aws-ocr-tesseract-demo.git
```

- Deploy the lambda
```
sls deploy --aws-profile nombre-de-nuestro-profile --stage dev
```

- Call lambda function
```
serverless invoke --function hello --aws-profile name-you-profile
```

- Remove Stack
```
serverless remove --stage dev --aws-profile
```

## API Security

In the deploy process the serverless framewokr show the ApiKey value in the console.

```bash
Deploying lambda-bedrock-proxy to stage dev (us-east-1)

✔ Service deployed to stack lambda-bedrock-proxy-dev (80s)
# Value of APIKEY
api keys:
  tollmkey: YOURAPIKEYHERE - tollmkey api key# Optional
endpoint: GET - https://xxxxxxxxxx.execute-api.us-east-1.amazonaws.com/dev/titan
functions:
  hello: lambda-bedrock-proxy-dev-hello (3.1 kB)
layers:
  bedrock: arn:aws:lambda:us-east-1:XXXXXXXXX:layer:bedrock-dependencies:4
```

How invoke the endpoint securized with API key

```bash
curl --location 'https://xxxxxxx.execute-api.us-east-1.amazonaws.com/dev/titan' \
--header 'x-api-key: YOURAPIKEYHERE'
```
