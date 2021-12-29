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

from flask import Blueprint, jsonify, Flask, request
from utils import *
accountApi = Blueprint('accountApi', __name__, url_prefix='/account')


@accountApi.route('/accountValue', methods=['POST', 'GET'])
def getAccountValue():
    if request.method == 'POST':
        address = request.form['address']
        print(address)
        args = [to_checksum_address(address)]
        res = client.call(to_address, contract_abi, "getAccountValue", args)
        if res[0] < 0:
            return jsonify({'Message': "Error occurs when getting account value"})
        return jsonify({'accountValue': res[1]})
    return jsonify({'Exception': testStr})


@accountApi.route('/accountType', methods=['POST', 'GET'])
def getAccountType():
    if request.method == 'POST':
        address = request.form['address']
        print(address)
        args = [to_checksum_address(address)]
        res = client.call(to_address, contract_abi, "getAccountType", args)
        if res[0] < 0:
            return jsonify({'Message': "Error occurs when getting account type"})
        if res[1] == 0:
            ret = 'Company'
        elif res[1] == 1:
            ret = 'Finance'
        return jsonify({'accountType': ret})
    return jsonify({'Exception': testStr})


@accountApi.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        print("enter into post method!!!")
        '''获取用户名密码'''
        username, password = request.form['username'], request.form['password']
        '''获取其他参数'''
        accType = request.form.get('acctype', 'Company') # 默认为Company类
        inivalue = request.form.get('value', 0) # 默认为0
        if accType == 'Company':
            accType = 0
        elif accType == 'Finance':
            accType = 1
        '''用户名长度上限'''
        max_account_len = 100
        '''过长，抛出异常'''
        if len(username) > max_account_len:
            return jsonify({'Exception': 'The name should be less than 240 characters!'})
        print("starting : {} {} ".format(username, password))
        '''通过密码生成账户，包括账户地址、公私钥'''
        ac = Account.create(password)
        '''生成signer'''
        signer = Signer_ECDSA(ac)
        print("address :\t", ac.address)
        print("privkey :\t", encode_hex(ac.key))
        print("pubkey :\t", ac.publickey)

        '''根据密码和私钥生成账户kf'''
        kf = Account.encrypt(ac.privateKey, password)
        '''keystore文件存放地址'''
        keyfile = "{}/{}.keystore".format(client_config.account_keyfile_path, username)
        print("save to file : [{}]".format(keyfile))
        '''写入keyfile'''
        with open(keyfile, "w") as dump_f:
            '''将私钥写入'''
            json.dump(kf, dump_f)
            dump_f.close()
        print(
            "INFO >> Read [{}] again after new account,address & keys in file:".format(keyfile))

        '''参数包'''
        args = [int(inivalue), int(accType)]
        '''调用链端函数'''
        receipt = client.sendRawTransactionGetReceipt(to_address,contract_abi, "register", args, from_account_signer=signer)
        return jsonify({'Status': 'Successfully registered!', 'Address': ac.address, 'Pubkey': str(ac.publickey), 'Privkey': str(encode_hex(ac.key))})


    return jsonify({'Exception': testStr})
