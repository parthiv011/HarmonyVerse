import base64,requests,json

URL = "https://accounts.spotify.com/api/token?grant_type=client_credentials"
encoded = base64.b64encode('2e5500d800e546bd8ee1d308a15ba879:8e33cbd07e364a7984a3a1143c62bb19'.encode('utf-8')).decode()
headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Authorization': 'Basic '+encoded
}

response = requests.request("POST", URL, headers=headers).json()

print(json.dumps(response, indent=4))