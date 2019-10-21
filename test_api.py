import requests

r = requests.post("http://localhost:5000", json={"key": "value"})
print(r.json())
