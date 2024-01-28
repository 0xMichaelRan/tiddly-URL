# tinyURL

tinyURL是以flask为基础实现的一个http短链接服务。该项目提供了短链接生成和还原、短链接访问统计、API服务、用户鉴权这几项功能。

## 导航

- [设计思路](#设计思路)
- [代码架构](#代码架构)
- [项目框架](#项目框架)
- [安装](#安装)
- [使用](#使用)

## 设计思路

- 生成短链接设计思路类似于进制转换。将一条URL所对应自增id进行对编码集长度取余,从而保证生成短链接唯一(例如一条URL的id为125，假设编码集为十六进制，则短链接为7D)。对于本项目编码集而言,长度为5的短链接可对应3亿左右条数的数据。
- 对用户页面采用密码方式鉴权，而对API接口采用Token方式鉴权。

## 代码架构

### 逻辑架构

| 包         | 描述                             |
| ---------- | -------------------------------- |
| api        | 提供API接口服务                  |
| main       | 提供用户相关服务以及相关视图渲染 |
| Change     | 存放生成短链接的算法             |
| decorators | 业务相关的装饰器                 |
| models     | 建立数据库对应模型               |
| apitest    | 对api接口的测试                  |
| manage     | 项目入口                         |
| ReadConfig | 读取配置信息                     |

### 数据库架构

![pic](https://github.com/zstone12/URL_Shortener/blob/master/app/static/db_pic.png)

## 项目框架

麻雀虽小五脏俱全，本项目框架简单关系如下图:

![pic2](https://github.com/zstone12/URL_Shortener/blob/master/app/static/arr_pic.jpg)

## 安装

~~~shell
pip3 install -r ruquirements.txt
~~~

## 使用

~~~shell
vim config.json #自行修改配置信息
export FLASK_APP=manage.py 
flask init-db #初始化数据库
python3 manage.py #项目启动
~~~
