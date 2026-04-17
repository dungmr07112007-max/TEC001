import requests
import json

url = f"http://127.0.0.1:5000/airport/VVTS"
response = requests.get(url).json()

print(json.dumps(response, indent=2))