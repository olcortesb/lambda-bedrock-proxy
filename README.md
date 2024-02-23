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
