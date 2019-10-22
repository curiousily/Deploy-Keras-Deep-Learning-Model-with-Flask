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

TEST_URL = "http://localhost:5000"

r = requests.post(TEST_URL, json=data)
print(r.json())
