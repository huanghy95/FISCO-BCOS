pragma solidity ^0.4.25;
pragma experimental ABIEncoderV2;

import './Table.sol';

contract Credit{

// === private ====

function createTable() private {
    TableFactory tf = TableFactory(0x1001);
    tf.createTable("credit_asset", "account", "value,type");
    tf.createTable("credit_bill", "id", "debtor,creditor,value,status");
    tf.createTable("credit_creditor", "creditor", "id");
    tf.createTable("credit_debtor", "debtor", "id");
}

function openAssetTable() private returns(Table){
    TableFactory tf = TableFactory(0x1001);
    Table table = tf.openTable("credit_asset");
    return table;
}

function openBillTable() private returns(Table){
    TableFactory tf = TableFactory(0x1001);
    Table table = tf.openTable("credit_bill");
    return table;
}

function openCreditorTable() private returns(Table){
    TableFactory tf = TableFactory(0x1001);
    Table table = tf.openTable("credit_creditor");
    return table;
}

function openDebtorTable() private returns(Table){
    TableFactory tf = TableFactory(0x1001);
    Table table = tf.openTable("credit_debtor");
    return table;
}

function getAccount(address account) private view
returns(int256, Entry){
    Table table = openAssetTable();
    Entries entries = table.select(toAsciiString(account), table.newCondition());
    if (entries.size() == 0){
        return (-1, table.newEntry());
    }
    else {
        Entry entry = entries.get(0);
        return (0, entry);
    }
}

function getBill(string id) private view
returns (int256, Entry){
    Table table = openBillTable();
    Entries entries = table.select(id, table.newCondition());
    if (entries.size() == 0){
        return (-1, table.newEntry());
    }
    else{
        Entry entry = entries.get(0);
        return (0, entry);
    }
}

function toAsciiString(address x) internal pure returns (string memory) {
    bytes memory s = new bytes(40);
    for (uint i = 0; i < 20; i++) {
        bytes1 b = bytes1(uint8(uint(uint160(x)) / (2**(8*(19 - i)))));
        bytes1 hi = bytes1(uint8(b) / 16);
        bytes1 lo = bytes1(uint8(b) - 16 * uint8(hi));
        s[2*i] = char(hi);
        s[2*i+1] = char(lo);            
    }
    return string(s);
}

function char(bytes1 b) internal pure returns (bytes1 c) {
    if (uint8(b) < 10) return bytes1(uint8(b) + 0x30);
    else return bytes1(uint8(b) + 0x57);
}


// === public ====

constructor() public{
    createTable();
}

// --- Enum ---
enum AccountType { Company, Finance }
enum BillStatus { Unpayed, Payed, Invalid }

// --- Getters ---

// 获取账户信用余额
function getAccountValue(address account) public view
returns(int256, uint256) {
    int256 code;
    Entry entry;
    Table table = openAssetTable();
    Entries entries = table.select(toAsciiString(account), table.newCondition());
    (code, entry) = getAccount(account);
    if (code < 0){
        return (code, 0);
    }
    else{
        return (code,uint256(entry.getUInt("value")));
    }
}

// 获取账户类型
function getAccountType(address account) public view
returns(int256 ,AccountType){
    int256 code;
    Entry entry;
    (code, entry) = getAccount(account);
    if (code < 0){
        return (code, AccountType.Company);
    }
    else{
        return (code, AccountType(entry.getUInt("type")));
    }
}

// 获取欠条债务人
function getBillDebtor(string id) public view
returns(int256, address) {
    int256 code;
    Entry entry;
    (code, entry) = getBill(id);
    if (code < 0){
        return (code, address(0));
    }
    else{
        return (code, entry.getAddress("debtor"));
    }
}

// 获取欠条债权人
function getBillCreditor(string id) public view
returns(int256, address){
    int256 code;
    Entry entry;
    (code, entry) = getBill(id);
    if (code < 0){
        return (code, address(0));
    }
    else{
        return (code, entry.getAddress("creditor"));
    }
}

// 获取欠条欠款值
function getBillValue(string id) public view
returns(int256, uint256) {
    int256 code;
    Entry entry;
    (code, entry) = getBill(id);
    if (code < 0){
        return (code, 0);
    }
    else{
        return (code, uint256(entry.getUInt("value")));
    }
}

// 获取欠条状态
function getBillStatus(string id) public view
returns(int256, BillStatus){
    int256 code;
    Entry entry;
    (code, entry) = getBill(id);
    if (code < 0){
        return (code, BillStatus.Invalid);
    }
    else{
        return (code, BillStatus(entry.getUInt("status")));
    }
}

/**
 * 账户注册
 * @param value : 初始信用额度
 * @param acc_type : 账户类型
 * 调用者地址自动成为账户地址
 */
function register(uint256 value, uint256 acc_type) public returns(int256){
    Table table = openAssetTable();
    string memory acc = toAsciiString(msg.sender);
    Entries entries = table.select(acc, table.newCondition());
    if (entries.size() != 0){
        return -1;
    }
    
    Entry entry = table.newEntry();
    entry.set("account", acc);
    entry.set("value", value);
    entry.set("type", acc_type);
    
    int count = table.insert(acc, entry);
    
    if (count == 1)
        return 0;
    else
        return -2;
}

/**
 * 签订欠条
 * @param id : 欠条id
 * @param creditor : 债权人
 * @param value : 欠款值
 * 调用者自动成为债务人
 */
function addBill(string id, address creditor, uint256 value) public
returns(int256) {
    if (creditor == msg.sender){
        // no self-debt
        return -6;
    }
    int256 code;
    Entry entry;
    Entry entry_debtor;
    Entry entry_creditor;
    (code, entry) = getBill(id);
    if (code == 0){
        // id exists
        return -1;
    }
    uint256 rest_value;
    (code, entry_debtor) = getAccount(msg.sender);
    if (code < 0){
        // debtor not exists
        return -2;
    }
    rest_value = uint256(entry_debtor.getInt("value"));
    if (value > rest_value){
        // not enough value
        return -3;
    }
    (code, entry_creditor) = getAccount(creditor);
    if (code < 0){
        // creditor not exists
        return -4;
    }
    if (AccountType(entry_debtor.getInt("type")) == AccountType.Finance
    && AccountType(entry_creditor.getInt("type")) == AccountType.Company){
        // Finance should not borrow from Company
        return -5;
    }
    
    Table table = openBillTable();
    Table table_d = openDebtorTable();
    Table table_c = openCreditorTable();
    Table table_a = openAssetTable();
    
    entry = table.newEntry();
    entry.set("id", id);
    entry.set("creditor", creditor);
    entry.set("debtor", msg.sender);
    entry.set("value", value);
    entry.set("status", uint256(BillStatus.Unpayed));
    table.insert(id, entry);
    
    
    entry = table_d.newEntry();
    entry.set("debtor", toAsciiString(msg.sender));
    entry.set("id", id);
    table_d.insert(toAsciiString(msg.sender), entry);
    
    entry = table_c.newEntry();
    entry.set("id", id);
    entry.set("creditor", toAsciiString(creditor));
    table_c.insert(toAsciiString(creditor), entry);
    
    
    entry_debtor.set("value", rest_value-value);
    table_a.update(entry_debtor.getString("account"), entry_debtor, table_a.newCondition());
    
    return 0;
}
/**
 * 分割-转移欠条
 * @param old_id : 原有欠条id
 * @param new_id : 分割出来的新欠条id
 * @param new_creditor : 新欠条的债权人
 * @param new_value 新欠条的欠款值
 * 调用者必须是债权人
 */
function transferBill(string old_id, string new_id, address new_creditor, uint256 new_value) 
public returns(int256){
    Entry old_bill;
    int code;
    (code, old_bill) = getBill(old_id);
    if (code < 0){
        // old_bill not exists
        return -1;
    }
    address creditor = old_bill.getAddress("creditor");
    if (creditor != msg.sender){
        // sender not the creditor
        return -2;
    }
    uint256 old_value = uint256(old_bill.getInt("value"));
    if (old_value < new_value){
        // not enough old value
        return -3;
    }
    
    Entry entry; (code, entry) = getBill(new_id);
    if (code == 0){
        // new id exists
        return -4;
    }
    
    (code, entry) = getAccount(new_creditor);
    if (code < 0){
        // no such new creditor
        return -5;
    }
    
    address debtor = old_bill.getAddress("debtor");
    
    Table table = openBillTable();
    old_bill.set("value", old_value - new_value);
    table.update(old_id, old_bill, table.newCondition());
    
    entry = table.newEntry();
    entry.set("id", new_id);
    entry.set("creditor", new_creditor);
    entry.set("debtor", debtor);
    entry.set("value", new_value);
    entry.set("status", uint256(BillStatus.Unpayed));
    table.insert(new_id, entry);
    
    table = openDebtorTable();
    entry = table.newEntry();
    entry.set("debtor", toAsciiString(debtor));
    entry.set("id", new_id);
    table.insert(toAsciiString(debtor), entry);
    
    table = openCreditorTable();
    entry = table.newEntry();
    entry.set("creditor", toAsciiString(new_creditor));
    entry.set("id", new_id);
    table.insert(toAsciiString(new_creditor), entry);
    
    return 0;
    
}


/**
 * 支付信用额度融资
 * @param id : 欠条id
 * @param creditor_f : 债权人（必须是金融机构账户）
 * @param fvalue : 融资额
 * 调用者就是融资者，自动成为债务人
 */
function financeWithCredit(string id, address creditor_f, uint256 fvalue) public returns(int256){
    int code;
    Entry entry;
    (code, entry) = getAccount(creditor_f);
    if (code < 0){
        // no such creditor_f
        return -100;
    }
    if (AccountType(entry.getInt("type")) != AccountType.Finance){
        // not fiance
        return -200;
    }
    return addBill(id, creditor_f, fvalue);
}

/**
 * 分割-转移欠条来融资
 * @param old_id : 原有欠条id
 * @param new_id string : 分割出来的新欠条id
 * @param creditor_f : 新欠条的债权人（必须是金融机构
 * @param fvalue 融资额
 * 调用者必须是债权人
 */
function financeWithBillTransfered(string old_id, string new_id, address creditor_f, uint256 fvalue) public returns(int256){
    int code;
    Entry entry;
    (code, entry) = getAccount(creditor_f);
    if (code < 0){
        // no such creditor_f
        return -100;
    }
    if (AccountType(entry.getInt("type")) != AccountType.Finance){
        // not fiance
        return -200;
    }
    return transferBill(old_id, new_id, creditor_f, fvalue);
}


function payBack(string id) public returns(int256){
    int code;
    Entry bill;
    (code, bill) = getBill(id);
    if (code < 0){
        // bill not exists
        return -1;
    }
    address creditor = bill.getAddress("creditor");
    if (creditor != msg.sender){
        // sender not the creditor
        return -2;
    }
    if (BillStatus(bill.getInt("status")) != BillStatus.Unpayed){
        // not unpayed bill
        return -3;
    }
    
    bill.set("status", uint256(BillStatus.Payed));
    Table table_b = openBillTable();
    table_b.update(id, bill, table_b.newCondition());
    
    uint256 value = uint256(bill.getInt("value"));
    Entry e_debtor;
    (code, e_debtor) = getAccount(bill.getAddress("debtor"));
    e_debtor.set("value", uint256(e_debtor.getInt("value")) + value);
    Table table = openAssetTable();
    table.update(e_debtor.getString("account"), e_debtor, table.newCondition());
    
    Table table_d = openDebtorTable();
    Condition cond = table_d.newCondition();
    cond.EQ("id", id);
    table_d.remove(toAsciiString(bill.getAddress("debtor")), cond);
    
    Table table_c = openCreditorTable();
    cond = table_c.newCondition();
    cond.EQ("id", id);
    table_c.remove(toAsciiString(bill.getAddress("creditor")), cond);
    
    return 0;
}



// 查询给定债务人对应的所有欠条
function queryBillDebtor(address debtor) public view
returns(int256, string[]){
    
    string[] memory ids = new string[](0);
    Table table_acc = openAssetTable();
    Entries es_acc = table_acc.select(toAsciiString(debtor), table_acc.newCondition());
    if (es_acc.size() == 0){
        return (-1, ids);
    }

    Table table = openDebtorTable();
    Entries entries = table.select(toAsciiString(debtor), table.newCondition());
    ids = new string[](uint(entries.size()));
    for (int i = 0; i < int(entries.size()); i++){
        ids[uint(i)] = entries.get(i).getString("id");
    }
    return (0, ids);
}

// 查询给定债权人对应的所有欠条
function queryBillCreditor(address creditor) public view
returns(int256, string[]){
    
    string[] memory ids = new string[](0);
    Table table_acc = openAssetTable();
    Entries es_acc = table_acc.select(toAsciiString(creditor), table_acc.newCondition());
    if (es_acc.size() == 0){
        return (-1, ids);
    }

    Table table = openCreditorTable();
    Entries entries = table.select(toAsciiString(creditor), table.newCondition());
    ids = new string[](uint(entries.size()));
    for (int i = 0; i < int(entries.size()); i++){
        ids[uint(i)] = entries.get(i).getString("id");
    }
    return (0, ids);
}
}
