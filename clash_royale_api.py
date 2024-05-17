import requests
import json

#This is the json web token generated from your developer.clashroyale.com account
file = open("token.txt", "r")
token = file.read().strip('\n')
file.close()


# Example - Get Cards
base_url = "https://api.clashroyale.com/v1"
endpoint = "/cards"
query = {"Authorization": f"Bearer {token}"}
response = requests.get(base_url+endpoint, params=query)

with open("example_response.json", "w") as response_file:
    r: dict = response.json()

    # For pretty output
    p: str = json.dumps(r, indent=4)
    response_file.write(p)



# Get Player Information
player_tag = 'CV898UC9J'
endpoint = "players"
query = {"Authorization": f"Bearer {token}", "playerTag": f"{player_tag}"}
response = requests.get('https://api.clashroyale.com/v1/players/%23CV898UC9J', params=query)
request_url = f'https://api.clashroyale.com/v1/{endpoint}/%23{player_tag}'
response = requests.get(request_url, params=query).json()
response.keys()


# battle log

request_url = f'https://api.clashroyale.com/v1/{endpoint}/%23{player_tag}/battlelog'
response = requests.get(request_url, params=query).json()
response[0]['team'][0]['cards'][0]
response[0]['opponent']
