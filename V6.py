"""
和V5功能一样，只是利用request功能实现
利用parse模块模拟post请求
分析百度辞典
分析步骤
1.打开F12
2.尝试输入girl，发现每次桥一个字母都有请求
3.请求地址为http://fanyi.baidu.com/sug
4.利用Network-ALL，找到文件的url地址
5.
"""

import urllib.request,urllib.parse

import json

baseurl = 'https://fanyi.baidu.com/sug'

# 存放的用来模拟form的数据一定是dict模式
#**kw：表示就是形参中按照关键字传值，多余的值都给kw，且以字典*的方式呈现

data = {
    'kw': 'girl'
}
    # girl是翻译输入的英文内容，应该是用户输入，此四处使用硬编码

# 需要哟个parse模块对data进行编码

data = urllib.parse.urlencode(data).encode("utf-8")

print(type(data))

print(data)

# 我们需要构造一个请求头，请求头部至少包含传入的数据长度
#request需要川区的请求头是一个dict格式

headers= {
    #因为是post格式，至少应该包含content-length字段
    'Content-Length':len(data)
}

req = urllib.request.Request(url= baseurl,data = data,headers = headers)

# 因为已经构造了一个Request的请求实力，则所有的请求信息都可以封装在Request实力李
rsp = urllib.request.urlopen(req)

json_data = rsp.read().decode('utf-8')

#json.loads 用于解码 JSON 数据。该函数返回 Python 字段的数据类型
json_data = json.loads(json_data)
print(json_data)

for item in json_data['data']:
    print(item['k'],'...',item['v'])