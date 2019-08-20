import requests

# 两种请求方式

url = "https://www.baidu.com"
# 使用get请求
rsp = requests.get(url)
print(rsp.text)

# 使用requests请求

rsp = requests.request("get",url)
print(rsp.text)