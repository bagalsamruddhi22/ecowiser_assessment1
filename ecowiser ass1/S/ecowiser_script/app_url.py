import urllib.parse

# LinkedIn app credentials
client_id = "773bpq8j3s010d"  # Your LinkedIn Client ID
redirect_uri = "http://localhost:8000/callback"  # Must match the registered LinkedIn redirect URI
scope = "r_liteprofile r_emailaddress"  # Define the required OAuth permissions/scopes

# Construct the authorization URL
auth_url = "https://www.linkedin.com/oauth/v2/authorization?"
query_params = {
    "response_type": "code",
    "client_id": client_id,
    "redirect_uri": redirect_uri,
    "scope": scope,
}

# Create the full URL with query parameters
authorization_url = auth_url + urllib.parse.urlencode(query_params)

print("Visit this URL to authorize the application:")
print(authorization_url)  # Output the authorization URL