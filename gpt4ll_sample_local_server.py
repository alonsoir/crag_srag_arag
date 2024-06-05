import json

import requests

# Define the base URL for the local server running the model
# base_url = "http://localhost:4891/v1"
# Define the base URL for the mitm proxy local server running the model
# mitmproxy --mode reverse:http://localhost:4891 --listen-host 127.0.0.1 --listen-port 8080
base_url = "http://localhost:8080/v1"

# Set up the prompt and other parameters for the API request
prompt = "Who is Michael Jordan?"
model = "Mistral-7B-Instruct-v0.1.Q4_0.GGUF"

# Prepare the request payload
payload = {
    "model": model,
    "prompt": prompt,
    "max_tokens": 50,
    "temperature": 0.28,
    "top_p": 0.95,
    "n": 1,
    "echo": True,
    "stream": False,
}

# Log the request details
print("Sending request to:", base_url)
print("Payload:", json.dumps(payload, indent=4))

# Make the API request to the local server
response = requests.post(f"{base_url}/completions", json=payload)

# Check if the request was successful
if response.status_code == 200:
    # Extract the completion from the response
    completion = response.json()
    print(f"prompt is {prompt}")
    print(json.dumps(completion, indent=4))
else:
    print(f"Error: {response.status_code}")
    print(response.text)
