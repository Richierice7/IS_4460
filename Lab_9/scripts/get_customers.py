import requests

api_url = 'http://localhost:8000/api/customers/'

token = 'a68cdb1d8ab00a9a671d7a33051f0ae391baedfb'

headers = {
    'Authorization': f'Token {token}'
}

response = requests.get(api_url, headers=headers)

print(response.status_code)

if response.status_code == 200:
    print(f"Customers retrieval successful. {response.text}")
else:
    print(f"Customers retrieval failed. {response.text}")