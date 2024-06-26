from flask import Flask
from flask_cors import CORS
app = Flask(__name__)

app.config.from_object(__name__)
CORS(app, resources={r"/*":{'origins':"*"}})

#Routes
@app.route('/', methods=['GET'])
def greetings():
    return("Hello, world!")

@app.route('/Login', methods=['PUT'])
def shark():
    return("Shark🦈!")

if __name__ == "__main__":
    app.run(debug=True)
