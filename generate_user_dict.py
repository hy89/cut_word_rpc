# @Author: hy
# @Time: 2020-01-07 11:16
# 生成用户自定义词典
import pymysql

from conf import read_mysql_config, BASE_DIR


def user_dict():
    conn = pymysql.connect(**read_mysql_config)
    cursor = conn.cursor()
    sql = "select kw from gl_jiebafengci_kw order by id asc;"
    cursor.execute(sql)
    kws = cursor.fetchall()

    with open(BASE_DIR + '/userdict.txt', 'w', encoding='utf-8') as f:
        n = 1
        for kw in kws:
            if n == len(kws):
                f.write(kw[0] + ' nz')
            else:
                f.write(kw[0] + ' nz\n')
            n += 1


if __name__ == '__main__':
    user_dict()
