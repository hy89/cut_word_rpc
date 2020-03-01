# 自定义分词服务
import sys

sys.path.append('../')
import json

import grpc
import time

import jieba
import jieba.posseg as pseg
from concurrent import futures
from conf import BASE_DIR
from server.cutword_rpc import cutword_rpc_pb2, cutword_rpc_pb2_grpc
from generate_user_dict import user_dict
from server.rpc_conf import CUSTOM_PORT, _HOST, _ONE_DAY_IN_SECONDS
from stop_words import stopwords_file

# 先生成userdict.txt文件
user_dict()

# 生成停用词文件
kw_set = stopwords_file()

# 加载停用词，停用词要结合固定方法使用，详情见官方demo
# jieba.analyse.set_stop_words()  


# 加载自定义词典到jieba
jieba.load_userdict(BASE_DIR + '/userdict.txt')


class Cut(cutword_rpc_pb2_grpc.CutServicer):
    def DoCut(self, request, context):
        title = request.text
        words = jieba.cut(title, cut_all=True)
        return_words = []
        for w in words:
            # 去掉停用词
            if w in kw_set:
                continue
            ret = pseg.lcut(w)
            for word, flag in ret:
                # ns 地名,n 名词, nr 人名,nz 其他专名,nt 机构团体名, vn 名动词, v 动词, q 量词,f 方位词,r 代词
                if flag in {'ns', 'n', 'nr', 'nz', 'nt'}:
                    return_words.append((word, flag))

        return_words = json.dumps(return_words)
        return cutword_rpc_pb2.Data(text=return_words)


def serve():
    grpcServer = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
    cutword_rpc_pb2_grpc.add_CutServicer_to_server(Cut(), grpcServer)
    grpcServer.add_insecure_port(_HOST + ':' + CUSTOM_PORT)
    grpcServer.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        grpcServer.stop(0)


if __name__ == '__main__':
    serve()
