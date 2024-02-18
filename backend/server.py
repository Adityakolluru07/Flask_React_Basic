from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/members')
def member():
    return {"member" : ['member1', 'member2', 'member3']}

if __name__ == "__main__":
    app.run(debug=True)