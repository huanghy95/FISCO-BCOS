from client.datatype_parser import DatatypeParser
from client.bcosclient import BcosClient

abi_file = "contracts/Credit.abi"
data_parser = DatatypeParser()
data_parser.load_abi_file(abi_file)
contract_abi = data_parser.contract_abi
client = BcosClient()
'''替换为合约地址'''
to_address = '0x42883e01ac97a3a5ef8a70c290abe0f67913964e'
testStr = "This is a test"
