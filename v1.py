
from urllib import request

if __name__ == '__main__':
    url = "https://www.7160.com/zhenrenxiu/42630/"
    # 打开相应url并把相应的页面作为返回
    rsp = request.urlopen(url)
    # 把返回的结果读取出来
    # 把读取的内容类型为bytes
    html = rsp.read()

    html = html.decode('utf-8','ignore')

    print(html)
