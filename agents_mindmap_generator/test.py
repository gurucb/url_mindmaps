import requests

url = "https://kirthikarajaganeshcognitive.openai.azure.com/openai/deployments/gpt-4o-mini/chat/completions?api-version=2023-03-15-preview"
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer 3e328fb1d0a3439990774cb1543bae17"
}
data = {
    "messages": [{"role": "user", "content": "Hello, how are you?"}],
    "max_tokens": 50
}

response = requests.post(url, headers=headers, params={'api-key': "3e328fb1d0a3439990774cb1543bae17" }, json=data)

if response.status_code == 200:
    print("Response:", response.json())
else:
    print("Error:", response.status_code, response.text)
