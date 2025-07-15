# Solace Ryan Pacheco Challenge
## Repo Contents
This repository contains code to bootstrap the AWS backend and also the client to call the endpoint. The client is located in the `client/` directory, everything else is infrastructure for the AWS lambda/API gateway deploy. 

### AWS Lambda Setup
To deploy your own endpoint follow these steps
**This assumes you already have an AWS and Huggingface account with access tokens**
1. Store huggingface access token in parameter store in a parameter named `/huggingface`
2. Unzip `openai-layer.zip`
3. run `cdk deploy`
4. Lambda is now ready to run

### Client Running
To run the client follow these steps
1. Navigate to `client/`
2. Run `python client.py`
3. Follow the screen prompts to send message to the LLM