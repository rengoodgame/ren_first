'''
爬虫豆瓣电影
熟悉ajax技术
'''
import urllib.request
import json
url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=60&limit=20"
rsp = urllib.request.urlopen(url)
data = rsp.read().decode()
data = json.loads(data)
print(data)


