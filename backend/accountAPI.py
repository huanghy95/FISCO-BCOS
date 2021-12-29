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
    if res[0] < 0:
        return jsonify({'Message': "Error occurs when getting account value"})
    return jsonify({'accountValue': res[1]})


@accountApi.route('/accountType', methods=['POST'])
def getAccountType():
    data = request.get_data()
    data = json.loads(data)
    to_address = data['to_address']
    address = data['address']
    args = [to_checksum_address(address)]
    res = client.call(to_address, contract_abi, "getAccountType", args)
    if res[0] < 0:
        return jsonify({'Message': "Error occurs when getting account type"})
    return jsonify({'accountType': res[1]})


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
    try:
        signer = getSigner(name, password)
    except ValueError:
        return jsonify({'Message': "Name and password mismatch."})

    receipt = client.sendRawTransactionGetReceipt(
        to_address, contract_abi, "register", args, from_account_signer=signer)
    
    return jsonify({'receipt': receipt})
