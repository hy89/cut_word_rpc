import pymysql

from conf import read_mysql_config, BASE_DIR


def stopwords_file():
    """生成停用词文件"""
    conn = pymysql.connect(**read_mysql_config)
    cursor = conn.cursor()
    # 读取停用词,构建停用词列表
    cursor.execute('select kw from gl_jieba_stop_kw order by id asc;')
    kws = cursor.fetchall()
    kw_set = set()
    with open(BASE_DIR + '/stopwords.txt', 'w', encoding='utf-8') as f:
        n = 1
        for kw in kws:
            if n == len(kws):
                f.write(kw[0])
                f.write("\n锅炉")  # 单独添加锅炉到词汇中
            else:
                f.write(kw[0] + '\n')
            n += 1
            kw_set.add(kw[0])
    kw_set.add("锅炉")
    cursor.close()
    conn.close()
    return kw_set


if __name__ == '__main__':
    stopwords_file()
