from flask import Blueprint, jsonify, Flask, request
import json
from backend.utils import client, contract_abi, getSigner, to_checksum_address
accountApi = Blueprint('accountApi', __name__, url_prefix='/account')


@accountApi.route('/accountValue', methods=['POST'])
def getAccountValue():
    data = request.get_data()
    data = json.loads(data)
    to_address = data['to_address']
    address = data['address']
    args = [to_checksum_address(address)]
    res = client.call(to_address, contract_abi, "getAccountValue", args)
    return jsonify({'accountValue': res})


@accountApi.route('/accountType')
def getAccountType():
    return jsonify({'Exception': "Not Implemented Yet"})


@accountApi.route('/register', methods=['POST'])
def register():
    data = request.get_data()
    data = json.loads(data)
    to_address = data['to_address']
    value = int(data['value'])
    acc_type = data['acc_type']
    if acc_type == 'Company':
        acc_type = 0
    elif acc_type == 'Finance':
        acc_type = 1
    args = [value, acc_type]

    name = data['name']
    password = data['password']
    signer = getSigner(name, password)

    receipt = client.sendRawTransactionGetReceipt(
        to_address, contract_abi, "register", args, from_account_signer=signer)
    return jsonify({'receipt': receipt})
