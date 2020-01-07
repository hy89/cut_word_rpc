### 根目录下说明
`stop_words.py` 用来获取停用词集合,会生成`stopwords.txt`文件

`generate_user_dict.py` 用来生成自定义词典文件 `userdict.txt`

`conf.py` 一些简单配置

`client.py` rpc客户端测试代码,调用rpc服务的代码参考该文件内代码实现

### server目录说明
`custom_cut_server.py` 是自定义词典分词的rpc服务代码,其中加载了自定义分词,并使用停用词和词性进行了过滤

`rpc_conf.py` 是rpc服务的几个配置项

### 运行
1.根据需要配置 `conf.py` 内数据库信息和server目录内`rpc_conf.py`信息

2.运行server目录内的`custom_cut_server.py`启动rpc服务端

3.运行`client.py` 测试


### grpc安装说明
```python
pip install grpcio
pip install protobuf
pip install grpcio-tools
```