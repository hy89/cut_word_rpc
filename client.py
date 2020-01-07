# @Author: hy
# @Time: 2020-01-07 10:21
import json

import grpc
from server.rpc_conf import _HOST, CUSTOM_PORT
from server.cutword_rpc import cutword_rpc_pb2_grpc, cutword_rpc_pb2


def custom_cut(title):
    conn = grpc.insecure_channel(_HOST + ':' + CUSTOM_PORT)
    client = cutword_rpc_pb2_grpc.CutStub(channel=conn)
    response = client.DoCut(cutword_rpc_pb2.Data(text=title))
    # print("received: " + response.text)  # 打印接受到的响应信息
    # 数据转换还要
    keywords = json.loads(response.text)
    print(keywords)
    return keywords


if __name__ == '__main__':
    custom_cut("一个生物质锅炉有什么用途")

