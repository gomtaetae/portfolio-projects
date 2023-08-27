from flask import Flask
from flask_restx import Api
from flask_cors import CORS
import users

app = Flask(__name__)
CORS(app, origins="*")

@app.route("/")
def welcome():
    return "Welcome!"

api = Api(app, version='1.0', title='My App API',
          description='A simple My App API',
          doc='/api/')

# Add the namespaces
api.add_namespace(users.ns)

if __name__ == '__main__':
    app.run(port=5003, debug=True)