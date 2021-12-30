from flask import Flask, request
from flask import jsonify
from flask_cors import CORS
from accountAPI import accountApi
from billAPI import billAPI

from client.contractnote import ContractNote
from client.bcosclient import BcosClient
from eth_utils import to_checksum_address
from eth_utils.hexadecimal import encode_hex
from eth_account.account import Account
from client.datatype_parser import DatatypeParser
from client.common.compiler import Compiler
from client.bcoserror import BcosException, BcosError
from client_config import client_config

from client.signer_impl import *

from utils import *

import json

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
    return {'time': "fuck ztl"}




if __name__ == '__main__':
    app.run()
