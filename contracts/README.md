# 使用合约代码

## Step 1

将整个contracts文件夹复制到python-sdk文件夹内。

**下面全部操作假设在python-sdk文件夹中执行**

## Step 2

准备`solc`编译器

将`solc`文件复制到`bin/solc/v0.4.25/`文件夹中

## Step 3

配置`solc`路径。

编辑`client_config.py`，增加一条：
```
solc_path = "./bin/solc/v0.4.25/solc"
```

## Step 4

编译部署合约。

执行如下命令：
```
python console.py deplay Credit
```

在返回中消息中找到合约地址，即可调用合约函数。
