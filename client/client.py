import requests

def call_lambda():
    url = "https://4ksum0zgs6.execute-api.us-east-1.amazonaws.com/prod/" # Change this URL to your own if you've deployed your own lambda
    while True:
        print("Enter message to Meta-Llama-3-8B-Instruct Model or 'END' to quit: ")
        message = input()
        if message == "END":
            break
        body = {
            "messages": [
                {"role": "user", "content": message},
            ]
        }
        response = requests.post(url, json=body).json()
        print(f"\n{response['response']}\n")


if __name__ == "__main__":
    call_lambda()
