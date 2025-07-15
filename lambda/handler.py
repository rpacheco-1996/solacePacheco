import os
from openai import OpenAI
import json
import boto3

ssm = boto3.client('ssm', region_name='us-east-1')
huggingParam = ssm.get_parameter(Name=os.environ["HF"], WithDecryption=False)

client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=huggingParam['Parameter']['Value'],
    default_headers={"x-use-provider": "novita"}
)

def callHuggingFace(messages):
    response = client.chat.completions.create(
            model="meta-llama/Meta-Llama-3-8B-Instruct",
            messages=messages
        )
    return response


def lambda_handler(event, context):
    body = json.loads(event.get("body", "{}"))
    messages = body.get("messages", [])
    try:
        huggingface = callHuggingFace(messages)
        return {
            "statusCode": 200,
            "body": json.dumps({
                "response": huggingface.choices[0].message.content
            })
        }
    except Exception as e: 
        return {
            "statusCode": 500,
            "body": str(e)
        }
