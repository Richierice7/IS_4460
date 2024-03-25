import requests
import json

id = 1

api_url = f'http://localhost:8000/api/orders/{id}/'

order_data = {
    "customer": 1,
    "total_price": "12.99",
    "total_items": "4"
    }

response = requests.put(api_url, data=json.dumps(order_data), headers={'Content-Type': 'application/json'})

if response.status_code == 200:
    print("Orders updated successfully.")
else:
    print("Error retrieving the orders.")