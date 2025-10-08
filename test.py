import requests

url = "https://api.intelligence.io.solutions/api/v1/chat/completions"

headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer io-v2-eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9."
    "eyJvd25lciI6IjIwMjViYTk0LTc5ZjItNDcxNi1iYjE2LTE5YjAxOWZlMjMxYiIsImV4cCI6NDkxMzQzMTMwMH0."
    "EVhhcbFKeK886IDRENAL6ajCQTzJkQBbVoD49gMsp1mWeB8CRm2ID2IzqUn4dHPCl5tu_4I5FpDPw6Nrk2Y9dw"
}

data = {
    "model": "meta-llama/Llama-3.2-90B-Vision-Instruct",
    "messages": [
        {
            "role": "system",
            "content": "You Jarvis"
        },
        {
            "role": "user",
            "content": "Who are you"
        }
    ]
}

response = requests.post(url, headers=headers, json=data)
data = response.json()

answer = data['choices'][0]['message']['content']
print(answer.split('</think>\n\n')[0]) 