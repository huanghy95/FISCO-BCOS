import os
import json
import traceback
from client.bcoserror import BcosException, BcosError
from client_config import client_config
from client.common.compiler import Compiler
from client.datatype_parser import DatatypeParser
from client.stattool import StatTool
from client.bcosclient import BcosClient
from client.signer_impl import *
from eth_utils import to_checksum_address

if os.path.isfile(client_config.solc_path) or os.path.isfile(client_config.solcjs_path):
    Compiler.compile_file("contracts/Credit.sol")
abi_file = "contracts/Credit.abi"
data_parser = DatatypeParser()
data_parser.load_abi_file(abi_file)
contract_abi = data_parser.contract_abi

client = BcosClient()


def getSigner(name, password):
    edcsa_account_file = "{}/{}.keystore".format(
        client_config.account_keyfile_path, name)
    signer = Signer_ECDSA.from_key_file(edcsa_account_file, password)
    return signer
