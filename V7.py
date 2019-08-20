'''
URLError

'''

import urllib.request,urllib.error

url = "http://www.baiidu.com"

try:
    req = urllib.request.Request(url)
    rsp = urllib.request.urlopen(req)
    html = rsp.read().decode()
    print(html)

except urllib.error.URLError as e:
    print("URLErr:{0}".format(e.reason))
    print("URLErr:{0}".format(e))

except Exception as e:
    print(e)