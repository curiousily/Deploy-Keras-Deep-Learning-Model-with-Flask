import requests

data = {
    "neighbourhood_group": "Brooklyn",
    "latitude": 40.64749,
    "longitude": -73.97237,
    "room_type": "Private room",
    "minimum_nights": 1,
    "number_of_reviews": 9,
    "calculated_host_listings_count": 6,
    "availability_365": 365
}

r = requests.post("http://localhost:5000", json=data)
print(r.json())
