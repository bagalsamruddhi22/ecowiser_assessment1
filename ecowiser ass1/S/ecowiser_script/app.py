from flask import Flask, request  # Import Flask and request handling components

# Initialize the Flask app
app = Flask(__name__)

# Define the route for LinkedIn's OAuth callback
@app.route('/callback')
def callback():
    # Get the authorization code from LinkedIn's query parameter
    authorization_code = request.args.get('code')
    
    # Check if authorization code is received
    if authorization_code:
        print("Authorization code:", authorization_code)  # Output the code
        # You might store this code to use in other scripts or return it in response
        return f"Authorization code received: {authorization_code}", 200
    else:
        return "No authorization code found", 400  # Handle the case where code is missing

# Ensure the Flask server starts on localhost, port 8000
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)  # Start the Flask server in debug mode