'''

使用代理访问百度
'''

import urllib.request, urllib.error

if __name__ == '__main__':
    url = 'http://www.baidu.com'

    # 使用代理步骤
    #设置代理地址
    proxy ={'http:':'120.194.18.90:81'}

    #创建ProxyHandler
    proxy_handler = urllib.request.ProxyHandler(proxy)

    # 创建Opener
    opener = urllib.request.build_opener(proxy_handler)

    # 安装Opener
    urllib.request.install_opener(opener)

    # 现在如果访问url,则使用的代理服务器

    try:
        rsp = urllib.request.urlopen(url)

        html = rsp.read().decode()
        print(html)

    except urllib.error.URLError as e:
        print(e)

    except Exception as e:
        print(e)