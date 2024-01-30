import os

"""
    #此脚本测试/shorten这一api接口，也同时起到一个往数据库中添加数据的作用。
"""
# command curl -i -X POST -H "Content-Type: application/json" -d '{"username":"ok","password":"python"}'
if __name__ == "__main__":
    str_raw = "https://www.zhihu.com/"
    api_address = "localhost/api/lengthen/ "
    api_key = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1ODU3NDIwMjUsIm5iZiI6MTU4NTc0MjAyNSwianRpIjoiN2JkYWFjNmYtMzc3ZS00ZGI5LWE0MGItODBjNDVkN2JiZTAyIiwiZXhwIjoxNTg1ODI4NDI1LCJpZGVudGl0eSI6MSwiZnJlc2giOmZhbHNlLCJ0eXBlIjoiYWNjZXNzIn0.4giQFtrvT5XEIEQJzQ1qchBpR6jRyIkg451twG5-JT8"
    api_key = '"Bearer' + " " + api_key + '"'
    for i in range(2):
        str_temp = str_raw + str(i)
        command = 'http {} Authorization:{} longurl="{}"'.format(
            api_address, api_key, str_temp
        )
        print(command)
        os.system(command)
