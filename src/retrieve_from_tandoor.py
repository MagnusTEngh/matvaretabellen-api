import requests
import json

token = "tda_11401e5d_a14d_47a7_ab70_31a017ac3e06"

r = requests.get(
    "http://192.168.0.184:3102/api/ingredient/",
    headers={"Authorization": f"Bearer {token}"},
)

print(json.dumps(r.json()["results"], indent=4))
