# Refresh the access token
import json,requests,base64

URL = "https://accounts.spotify.com/api/token?grant_type=refresh_token&refresh_token=AQAA1zbUU0THPi14TN7U-qT4XyEcq1_3Y0VOgfEFdRp_xzmaHy0tyRT0nlBDRO0zWT7WxLLIv5WUN3Qaz8W3MwqlMweP2r7VCiu9vAlmrF6C_7YsnH_9hQQCNX5Z3qvU-Mk"
encoded = base64.b64encode('2e5500d800e546bd8ee1d308a15ba879:8e33cbd07e364a7984a3a1143c62bb19'.encode('utf-8')).decode()
headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Authorization': 'Basic '+encoded
}

response = requests.request("POST", URL, headers=headers).json()

print(json.dumps(response, indent=4))
