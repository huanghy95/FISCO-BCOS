from flask import Blueprint, jsonify, Flask, request
from backend.utils import client, contract_abi
billAPI = Blueprint('billAPI', __name__, url_prefix='/bill')


@billAPI.route('/billDebtor')
def getBillDebtor():
    return jsonify({'Exception': "Not Implemented Yet"})


@billAPI.route('/billCreditor')
def getBillCreditor():
    return jsonify({'Exception': "Not Implemented Yet"})


@billAPI.route('/billValue')
def getBillValue():
    return jsonify({'Exception': "Not Implemented Yet"})


@billAPI.route('/billStatus')
def getBillStatus():
    return jsonify({'Exception': "Not Implemented Yet"})


@billAPI.route('/billDebtor')
def queryBillDebtor():
    return jsonify({'Exception': "Not Implemented Yet"})


@billAPI.route('/billCreditor')
def queryBillCreditor():
    return jsonify({'Exception': "Not Implemented Yet"})


@billAPI.route('/addBill', methods=['POST'])
def addBill():
    return jsonify({'Exception': "Not Implemented Yet"})


@billAPI.route('/transferBill', methods=['POST'])
def transferBill():
    return jsonify({'Exception': "Not Implemented Yet"})


@billAPI.route('/financeWithCredit', methods=['POST'])
def financeWithCredit():
    return jsonify({'Exception': "Not Implemented Yet"})


@billAPI.route('/financeWithBillTransfered', methods=['POST'])
def financeWithBillTransfered():
    return jsonify({'Exception': "Not Implemented Yet"})


@billAPI.route('/payBackBill', methods=['POST'])
def payBackBill():
    return jsonify({'Exception': "Not Implemented Yet"})
