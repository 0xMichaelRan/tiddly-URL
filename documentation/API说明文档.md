### 使用说明

URL_Shortener提供了[生成短链接](#生成短链接接口) 与[还原短链接](#还原短链接接口)两个接口。

使用前请了解如下事项：

- 使用接口前需要在用户界面获取API密钥，默认有效期为一天。

- API密钥需添加在请求头中，具体使用请查看请求示例。

### 生成短链接接口

##### 请求

~~~python
URL：http://129.204.185.247/api/shorten/
请求方式：POST
请求参数格式：JSON
~~~

### 请求参数说明

| 参数名   | 类型   | 是否必传 |                 描述 |
| -------- | ------ | -------- | -------------------: |
| long_url | string | 是       | 需要进行缩短的长网址 |

### 请求POST数据示例

~~~JSON
{
    "long_url": "https://www.baidu.com"
}	
~~~

### 请求示例

~~~python
http http://129.204.185.247/api/shorten/ Authorization:" Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1ODU2NjA0NjgsIm5iZiI6MTU4NTY2MDQ2OCwianRpIjoiYmE4YTJjMDMtNjBmOS00NzIxLWFjZmMtZmM2MWU5ZTRiYzI1IiwiZXhwIjoxNTg1NjYxMzY4LCJpZGVudGl0eSI6MSwiZnJlc2giOmZhbHNlLCJ0eXBlIjoiYWNjZXNzIn0.21oYWLZ9GgueJeCIzc9yUYgGjMCBgx7KKatpfIK-heo" long_url="https://www.baidu.com"
~~~

### 返回参数说明

| 名称 | 类型     | 描述     |
| ---- | -------- | -------- |
| code | interger | 返回码   |
| msg  | string   | 错误信息 |
| data | object   | 数据     |

### 数据 data

| 名称    | 类型   | 描述               |
| ------- | ------ | ------------------ |
| sid     | string | sid                |
| name    | string | 分组名称           |
| n_links | string | 该分组下的链接数量 |

### 返回结果示例

~~~json
{
    "code": 0,
    "data": {
        "location": "localhost/d",
        "long": "https://www.baidu.com",
        "short": "d"
    },
    "msg": "请求成功"
}

~~~

### 还原短链接接口

##### 请求

~~~python
URL：http://129.204.185.247/api/lengthen/
请求方式：POST
请求参数格式：JSON
~~~

### 请求参数说明

| 参数名   | 类型   | 是否必传 |                 描述 |
| -------- | ------ | -------- | -------------------: |
| long_url | string | 是       | 需要进行还原的短网站 |

###请求POST数据示例

~~~JSON
{
    "long_url": "129.204.185.247/5"
}	
~~~

### 请求示例

~~~python
http http://129.204.185.247/api/lengthen/ Authorization:" Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1ODU2NjA0NjgsIm5iZiI6MTU4NTY2MDQ2OCwianRpIjoiYmE4YTJjMDMtNjBmOS00NzIxLWFjZmMtZmM2MWU5ZTRiYzI1IiwiZXhwIjoxNTg1NjYxMzY4LCJpZGVudGl0eSI6MSwiZnJlc2giOmZhbHNlLCJ0eXBlIjoiYWNjZXNzIn0.21oYWLZ9GgueJeCIzc9yUYgGjMCBgx7KKatpfIK-heo" long_url="https://www.baidu.com"
~~~

### 返回参数说明

| 名称 | 类型     | 描述     |
| ---- | -------- | -------- |
| code | interger | 返回码   |
| msg  | string   | 错误信息 |

### 返回结果实例

~~~json
{
    "long": "http://www.zhihu.com",
    "msg": "请求成功"
}
~~~



