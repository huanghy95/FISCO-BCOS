# SYSU-2021BCOS-FinalProject

#### 启动FISCO BCOS链
- 启动所有节点
```shell
bash ./fisco/nodes/127.0.0.1/start_all.sh
```
- 启动成功会输出类似下面内容的响应。否则请使用netstat -an | grep tcp检查机器的30300~30303，20200~20203，8545~8548端口是否被占用。
```shell
try to start node0
try to start node1
try to start node2
try to start node3
 node1 start successfully
 node2 start successfully
 node0 start successfully
 node3 start successfully
```
- 检验进程是否启动
```shell
ps -ef | grep -v grep | grep fisco-bcos
```

- 启动控制台
```shell
cd ./fisco/console && bash start.sh
```

#### 配置python SDK
clone对应的python SDK
```shell
git clone https://github.com/FISCO-BCOS/python-sdk
```

写在脚本`ptsdk_checker.sh`里，可能需要给执行权限。
```shell
chmod +x ./pysdk_checker.sh && ./pysdk_checker.sh
```
验证是否配好：
```shell
cd ./python-sdk && python3 ./console.py getNodeVersion
```

详见文档：https://fisco-bcos-documentation.readthedocs.io/zh_CN/latest/docs/installation.html

---

#### 前后端运行命令

> backend

将 app.py 和 并将 backend 文件夹放进 python-sdk 中, 然后进入 python-sdk 文件夹运行下列命令.

``` bash
flask run
```
或者
``` bash
python3 app.py
```
> frontend
进入 frontend 文件夹执行以下命令.
install packages
``` bash
npm install 
```
run
```
npm run serve
```

