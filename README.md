# Solace Ryan Pacheco Challenge

## Background
I set up my project using `cdk init app --language python` I am using a lambda with an API gateway as the AWS host for the endpoint. It is wrapping a huggingface LLM and you can use the client or a curl request to interact with the LLM.

## Repo Contents
This repository contains code to bootstrap the AWS backend and also the client to call the endpoint. The client is located in the `client/` directory, everything else is infrastructure for the AWS lambda/API gateway deploy. 

## Setup
### AWS Lambda Setup (Only if you want your own endpoint)
To deploy your own endpoint follow these steps
**This assumes you already have an AWS and Huggingface account with access tokens**
1. Store huggingface access token in parameter store in a parameter named `/huggingface`
2. Unzip `openai-layer.zip`
3. run `cdk deploy`
4. Lambda is now ready to run

### Running the Client
To run the client follow these steps
1. Navigate to `client/`
2. Run `python client.py`
3. Follow the screen prompts to send message to the LLM