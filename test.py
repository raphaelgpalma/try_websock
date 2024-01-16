import requests
import jsonlines
import json

# Define the API key (replace this with your actual API key)
API_KEY = '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'

# Get the input from the user
user_input = input("Please enter the input: ")

# Prepare the request data to be sent to the GPT API
data = {
    'model': 'gpt-3.5-turbo',
    'stream': True,
    'messages': [
        {
            'role': 'user',
            'content': user_input
        }
    ]
}

# Set the headers for the request
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + API_KEY
}

# Send the request to the OpenAI API and process each chunk of data as it arrives
response = requests.post('https://api.openai.com/v1/chat/completions', data=json.dumps(data), headers=headers, stream=True)

if response.status_code == 200:
    with jsonlines.Reader(response.iter_lines()) as reader:
        for line in reader:
            # Extract and print the assistant's reply
            assistant_reply = line['choices'][0]['message']['content']
            print(assistant_reply)
else:
    print("Request failed with status code:", response.status_code)
