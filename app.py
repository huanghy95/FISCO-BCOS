from backend.billAPI import *
from backend.accountAPI import *
from flask_cors import CORS
from flask import jsonify
from flask import Flask, request
from backend.utils import *


app = Flask(__name__)
app.config['DEBUG'] = True
CORS(app, supports_credentials=True)
app.register_blueprint(accountApi)
app.register_blueprint(billAPI)

if __name__ == '__main__':
    app.run()
