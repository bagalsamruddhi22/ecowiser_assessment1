import requests

# LinkedIn app credentials
client_id = "773bpq8j3s010d"  # LinkedIn Client ID
client_secret = "qt1Uu3duGFAu4dBd"  # LinkedIn Client Secret
redirect_uri = "http://localhost:8000/callback"  # Must match the registered LinkedIn redirect URI

# The authorization code obtained from the OAuth callback
authorization_code = "YOUR_AUTHORIZATION_CODE"  # Replace with the code from app.py

# LinkedIn's OAuth 2.0 token endpoint
token_url = "https://www.linkedin.com/oauth/v2/accessToken"

# Data for the POST request to obtain the access token
data = {
    "grant_type": "authorization_code",
    "code": authorization_code,
    "redirect_uri": redirect_uri,
    "client_id": client_id,
    "client_secret": client_secret,
}

# Make the POST request to get the access token
response = requests.post(token_url, data=data)

if response.status_code == 200:
    token_data = response.json()
    access_token = token_data["access_token"]
    print("Access Token:", access_token)  # Output the access token
else:
    print("Failed to obtain access token")
    print("Status Code:", response.status_code)
    print("Error:", response.json())