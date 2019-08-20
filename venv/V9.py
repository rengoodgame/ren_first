'''

访问一个王之
更改自己的UserAgent进行伪装
'''

import urllib.request,urllib.error

if __name__ == '__main__':
    url = "http://www.baidu.com"
    try:
#使用headers进行为伪装
        headers = {}
        headers['User-Agent'] = 'Mozilla/5.0 (iPad; CPU OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3'
        req = urllib.request.Request(url,headers = headers)

#正常访问
        rsp = urllib.request.urlopen(req)

        html = rsp.read().decode()

        print(html)

    except urllib.error.HTTPError as e:
        print(e)
    except urllib.error.URLError as e:
        print(e)

    except Exception as e:
        print(e)

    print("DONE")