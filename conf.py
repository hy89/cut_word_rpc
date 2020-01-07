# @Author: hy
# @Time: 2019-09-24 10:05
# 读取title及自定义jieba词典的数据库地址
# import redis
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

read_mysql_config = {
    'host': '192.168.3.193',
    'port': 3306,
    'db': 'gl',
    'user': 'root',
    'passwd': 'abcd@1234',
    'charset': 'utf8mb4'
}
# 分词后的标签及标签与ask_id的关系写入的数据库地址
write_mysql_config = {
    'host': '192.168.3.193',
    'port': 3306,
    'db': 'gl',
    'user': 'root',
    'passwd': 'abcd@1234',
    'charset': 'utf8mb4'
}


