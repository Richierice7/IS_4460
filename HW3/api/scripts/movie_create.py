import requests
import json

api_url = 'http://localhost:8000/api/movies/'

movie_data = {
    "title": "Aladdin",
    "description": "A kind-hearted street urchin and a power-hungry Grand Vizier vie for a magic lamp that has the power to make their deepest wishes come true.",
    "director": "Ron Clements",
    "release_year": "1992",
    "budget": "$28 million",
    "runtime": "1h 30m",
    "rating": "G",
    "genre": "Animation/Adventure/Comedy"
}

response = requests.post(api_url, data=json.dumps(movie_data), headers={'Content-Type': 'application/json'})

if response.status_code == 201:
    print("Movies created successfully.")
else:
    print(f"Error creating movies.")