import requests                                 # library used to call the api
import json                                     # library used to handle json formats

apiKey = open("API_KEY.txt").read()             # get secret API key

headers = {                                     # used to pass data with request
    'Content-Type': 'application/json',         # specifies sending datatype
    'Authorization': 'Bearer ' + apiKey         # holds authorization information
}

data = json.dumps({
    "prompt": "Once upon a time",               # text gpt-3 will continue on
    "max_tokens": 15                            # specifies gpt-3's response length
})

result = requests.post(
    'https://api.openai.com/v1/engines/davinci/completions',    # endpoint
    headers=headers,
    data=data
)

print(result.json())                            # print result