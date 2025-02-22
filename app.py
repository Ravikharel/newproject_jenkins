from flask import Flask

# Create a Flask app
app = Flask(__name__)

# Define a route for the homepage
@app.route('/')
def home():
    return "Hello, World! Welcome to my Flask website."

# Run the app
if __name__ == '__main__':
    # Use your machine's IP address and set port (default is 5000)
    app.run(host='0.0.0.0', port=5000, debug=True)
