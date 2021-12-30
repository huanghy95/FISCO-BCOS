from client.contractnote import ContractNote
from client.bcosclient import BcosClient
from eth_utils import to_checksum_address
from eth_utils.hexadecimal import decode_hex
from eth_account.account import Account
from client.datatype_parser import DatatypeParser
from client.common.compiler import Compiler
from client.bcoserror import BcosException, BcosError
from client_config import client_config

from client.signer_impl import *

from utils import *

from flask import Blueprint, jsonify, Flask, request
billAPI = Blueprint('billAPI', __name__, url_prefix='/bill')


@billAPI.route('/billDebtor', methods=['POST', 'GET'])
def getBillDebtor():
    if request.method == 'POST':
        id = request.form['id']
        args = [str(id)]
        res = client.call(to_address, contract_abi, "getBillDebtor", args)
        if res[0] < 0:
            return jsonify({'Message': "Error occurs when getting bill debtor"})
        return jsonify({'debtor address': str(res[1])})
    return jsonify({'Exception': testStr})



@billAPI.route('/billCreditor', methods=['POST', 'GET'])
def getBillCreditor():
    if request.method == 'POST':
        id = request.form['id']
        args = [str(id)]
        res = client.call(to_address, contract_abi, "getBillCreditor", args)
        if res[0] < 0:
            return jsonify({'Message': "Error occurs when getting bill creditor"})
        return jsonify({'creditor address': str(res[1])})
    return jsonify({'Exception': testStr})


@billAPI.route('/billValue', methods=['POST', 'GET'])
def getBillValue():
    if request.method == 'POST':
        id = request.form['id']
        args = [str(id)]
        res = client.call(to_address, contract_abi, "getBillValue", args)
        if res[0] < 0:
            return jsonify({'Message': "Error occurs when getting bill value"})
        return jsonify({'bill value': str(res[1])})
    return jsonify({'Exception': testStr})


@billAPI.route('/billStatus', methods=['POST', 'GET'])
def getBillStatus():
    if request.method == 'POST':
        id = request.form['id']
        args = [str(id)]
        res = client.call(to_address, contract_abi, "getBillStatus", args)
        if res[0] < 0:
            return jsonify({'Message': "Error occurs when getting bill status"})
        ret = "Invalid"
        if res[1] == 0:
            ret = "Unpayed"
        elif res[1] == 1:
            ret = "Payed"
        elif res[1] == 2:
            ret = "Invalid"
        return jsonify({'bill status': ret})
    return jsonify({'Exception': testStr})


@billAPI.route('/queryBillDebtor', methods=['POST', 'GET'])
def queryBillDebtor():
    if request.method == 'POST':
        address = request.form['address']
        print(address)
        args = [to_checksum_address(address)]
        res = client.call(to_address, contract_abi, "queryBillDebtor", args)
        if res[0] < 0:
            return jsonify({'Message': "Error occurs when querying Bill Debtor"})
        return jsonify({'debated bill IDs': str(res[1])})
    return jsonify({'Exception': testStr})



@billAPI.route('/queryBillCreditor', methods=['POST', 'GET'])
def queryBillCreditor():
    if request.method == 'POST':
        address = request.form['address']
        print(address)
        args = [to_checksum_address(address)]
        res = client.call(to_address, contract_abi, "queryBillCreditor", args)
        if res[0] < 0:
            return jsonify({'Message': "Error occurs when querying Bill Creditor"})
        return jsonify({'credited bill IDs': str(res[1])})
    return jsonify({'Exception': testStr})



@billAPI.route('/addBill', methods=['POST', 'GET'])
def addBill():
    if request.method == 'POST':
        address = request.form['address']
        privkey = request.form['privkey']
        creditor = request.form['creditor']
        value = request.form['value']
        bid = request.form['bid']
        '''验证私钥'''
        ac = Account.from_key(privkey)
        if ac.address != address:
            return jsonify({'Message': "Wrong address or privkey"})
        '''根据私钥得到signer'''
        signer = Signer_ECDSA.from_privkey(decode_hex(privkey))
        args = [str(bid), to_checksum_address(creditor), int(value)]
        res = client.sendRawTransactionGetReceipt(to_address, contract_abi, "addBill", args, from_account_signer=signer)
        print(bid)
        if int(res['output'], 16) < pow(2, 255) :
            res = int(res['output'], 16)
        else:
            res = int(res['output'], 16) - pow(2,256)
        print(res)
        if res < 0:
            ret = "unknown wrong!"
            if res == -1:
                ret = "bill id has existed!"
            elif res == -2:
                ret = "debtor not exists!"
            elif res == -3:
                ret = "not enough value!"
            elif res == -4:
                ret = "creditor not exists!"
            elif res == -5:
                ret = "Finance should not borrow from Company!"
            return jsonify({'Message': ret, 'Status': res})
        return jsonify({'Message': "Successfully add bill!", "bid": bid})
    return jsonify({'Exception': testStr})


@billAPI.route('/transferBill', methods=['POST'])
def transferBill():
    if request.method == 'POST':
        address = request.form['address']
        privkey = request.form['privkey']
        new_creditor = request.form['new_creditor']
        new_value = request.form['new_value']
        old_id = request.form['old_id']
        new_id = request.form['new_id']

        '''验证私钥'''
        ac = Account.from_key(privkey)
        if ac.address != address:
            return jsonify({'Message': "Wrong address or privkey"})
        '''根据私钥得到signer'''
        signer = Signer_ECDSA.from_privkey(decode_hex(privkey))
        args = [str(old_id), str(new_id), to_checksum_address(new_creditor), int(new_value)]
        res = client.sendRawTransactionGetReceipt(to_address, contract_abi, "transferBill", args, from_account_signer=signer)
        if int(res['output'], 16) < pow(2, 255) :
            res = int(res['output'], 16)
        else:
            res = int(res['output'], 16) - pow(2,256)
        print(res)
        if res < 0:
            ret = "unknown wrong!"
            if res == -1:
                ret = "old_bill not exists!"
            elif res == -2:
                ret = "sender not the creditor!"
            elif res == -3:
                ret = "not enough old value!"
            elif res == -4:
                ret = "new id exists!"
            elif res == -5:
                ret = "no such new creditor!"
            return jsonify({'Message': ret, 'Status': res})
        return jsonify({'Message': "Successfully transfer bill!", "new_id": new_id})
    return jsonify({'Exception': testStr})


@billAPI.route('/financeWithCredit', methods=['POST'])
def financeWithCredit():
    if request.method == 'POST':
        address = request.form['address']
        privkey = request.form['privkey']
        creditor_f = request.form['creditor_f']
        fvalue = request.form['fvalue']
        bid = request.form['bid']
        '''验证私钥'''
        ac = Account.from_key(privkey)
        if ac.address != address:
            return jsonify({'Message': "Wrong address or privkey"})
        '''根据私钥得到signer'''
        signer = Signer_ECDSA.from_privkey(decode_hex(privkey))
        args = [str(bid), to_checksum_address(creditor_f), int(fvalue)]
        res = client.sendRawTransactionGetReceipt(to_address, contract_abi, "financeWithCredit", args, from_account_signer=signer)
        print(bid)
        if int(res['output'], 16) < pow(2, 255) :
            res = int(res['output'], 16)
        else:
            res = int(res['output'], 16) - pow(2,256)
        print(res)
        if res < 0:
            ret = "unknown wrong!"
            if res == -1:
                ret = "bill id has existed!"
            elif res == -2:
                ret = "debtor not exists!"
            elif res == -3:
                ret = "not enough value!"
            elif res == -4:
                ret = "creditor not exists!"
            elif res == -5:
                ret = "Finance should not borrow from Company!"
            elif res == -100:
                ret = "no such creditor_f!"
            elif res == -200:
                ret = "type not fiance!"
            return jsonify({'Message': ret, 'Status': res})
        return jsonify({'Message': "Successfully finance with credit!", "bid": bid})
    return jsonify({'Exception': testStr})


@billAPI.route('/financeWithBillTransfered', methods=['POST'])
def financeWithBillTransfered():
    if request.method == 'POST':
        address = request.form['address']
        privkey = request.form['privkey']
        creditor_f = request.form['creditor_f']
        fvalue = request.form['fvalue']
        old_id = request.form['old_id']
        new_id = request.form['new_id']

        '''验证私钥'''
        ac = Account.from_key(privkey)
        if ac.address != address:
            return jsonify({'Message': "Wrong address or privkey"})
        '''根据私钥得到signer'''
        signer = Signer_ECDSA.from_privkey(decode_hex(privkey))
        args = [str(old_id), str(new_id), to_checksum_address(creditor_f), int(fvalue)]
        res = client.sendRawTransactionGetReceipt(to_address, contract_abi, "financeWithBillTransfered", args, from_account_signer=signer)
        if int(res['output'], 16) < pow(2, 255) :
            res = int(res['output'], 16)
        else:
            res = int(res['output'], 16) - pow(2,256)
        print(res)
        if res < 0:
            ret = "unknown wrong!"
            if res == -1:
                ret = "old_bill not exists!"
            elif res == -2:
                ret = "sender not the creditor!"
            elif res == -3:
                ret = "not enough old value!"
            elif res == -4:
                ret = "new id exists!"
            elif res == -5:
                ret = "no such new creditor!"
            elif res == -100:
                ret = "no such creditor_f!"
            elif res == -200:
                ret = "type not fiance!"
            return jsonify({'Message': ret, 'Status': res})
        return jsonify({'Message': "Successfully finance with bill transfered!", "new_id": new_id})
    return jsonify({'Exception': testStr})


@billAPI.route('/payBackBill', methods=['POST'])
def payBackBill():
    if request.method == 'POST':
        address = request.form['address']
        privkey = request.form['privkey']
        bid = request.form['bid']
        '''验证私钥'''
        ac = Account.from_key(privkey)
        if ac.address != address:
            return jsonify({'Message': "Wrong address or privkey"})
        '''根据私钥得到signer'''
        signer = Signer_ECDSA.from_privkey(decode_hex(privkey))
        args = [str(bid)]
        res = client.sendRawTransactionGetReceipt(to_address, contract_abi, "payBack", args, from_account_signer=signer)
        print(bid)
        if int(res['output'], 16) < pow(2, 255) :
            res = int(res['output'], 16)
        else:
            res = int(res['output'], 16) - pow(2,256)
        print(res)
        if res < 0:
            return jsonify({'Message': "Something Wrong!"})
        return jsonify({'Message': "Successfully pay back!", "bid": bid})
    return jsonify({'Exception': testStr})
