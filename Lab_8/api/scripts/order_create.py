import requests
import json

api_url = 'http://localhost:8000/api/orders/'

order_data = {
    "customer": 1,
    "total_price": "24.99",
    "total_items": "3"
}

response = requests.post(api_url, data=json.dumps(order_data), headers={'Content-Type': 'application/json'})

if response.status_code == 201:
    print("Orders created successfully.")
else:
    print(f"Error creating orders.")