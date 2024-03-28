import requests
import json

id = 1

api_url = f'http://localhost:8000/api/movies/{id}/'

movie_data = {
    "title": "UP",
    "description": "78-year-old Carl Fredricksen travels to Paradise Falls in his house equipped with balloons, inadvertently taking a young stowaway.",
    "director": "Pete Docter",
    "release_year": "2009",
    "budget": "$175 million",
    "runtime": "1h 36m",
    "rating": "PG",
    "genre": "Animation/Adventure/Comedy"
}

response = requests.put(api_url, data=json.dumps(movie_data), headers={'Content-Type': 'application/json'})

if response.status_code == 200:
    print("Movies updated successfully.")
else:
    print(f"Error updating the movie.")