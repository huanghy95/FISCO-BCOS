from flask import Flask, request
from flask import jsonify
from flask_cors import CORS
from accountAPI import accountApi
from billAPI import billAPI

app = Flask(__name__)
app.config['DEBUG'] = True
CORS(app, supports_credentials=True)
app.register_blueprint(accountApi)
app.register_blueprint(billAPI)

@app.route('/getMsg', methods=['GET', 'POST'])
def home():
    response = {
        'msg': 'Hello, Python !'
    }
    return jsonify(response)


@app.route('/time')
def get_current_time():
    return {'time': "fuck hhy"}


if __name__ == '__main__':
    app.run()
