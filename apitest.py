import os
"""
    #此脚本测试/shorten这一api接口，也同时起到一个往数据库中添加数据的作用。
"""

if __name__ == '__main__':
    str_raw = 'long_url=https://www.zhihu.com/'
    for i in range(1000 ):
        str_temp = str_raw + str(i)
        command = 'curl localhost/shorten/ -X POST -d {}'.format(str_temp)
        os.system(command)
