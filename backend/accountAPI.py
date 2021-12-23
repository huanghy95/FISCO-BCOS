from flask import Blueprint, jsonify, Flask, request
accountApi = Blueprint('accountApi', __name__, url_prefix='/account')


@accountApi.route('/accountValue')
def getAccountValue():
    address = request.args.get('address')
    return jsonify({'address': address})


@accountApi.route('/accountType')
def getAccountType():
    return jsonify({'Exception': "Not Implemented Yet"})


@accountApi.route('/register', methods=['POST'])
def register():
    return jsonify({'Exception': "Not Implemented Yet"})
