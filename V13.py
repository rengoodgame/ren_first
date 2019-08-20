import urllib.request,urllib.parse

from http import cookiejar


cookie = cookiejar.CookieJar()

# 生成cookie管理其
cookie_handler= urllib.request.HTTPCookieProcessor(cookie)

# 创建http请求管理其

http_handler = urllib.request.HTTPHandler()

# 生成https管理其
https_handler = urllib.request.HTTPSHandler()

# 创建请求管理其
opener = urllib.request.build_opener(http_handler,https_handler,cookie_handler)

def login():
    '''

    负责初次登录
    需要输入用户名密码，用来获取登录cookie凭证
    :return:
    '''
    # 此url需要从登录form的action属性中提取
    url = "http://www.renren.com/PLogin.do"
    # 此建直需要从登录form的两个input 中提取name属性
    data = {
        "email:":"13119144223",
        "password":"123456"
    }

    # 把数据进行编码
    data = urllib.parse.urlencode(data)

    # 创建一个请求对象
    req = urllib.request.Request(url, data = data.encode())

    # 使用opener发起请求
    rsp = opener.open(req)

def getHomepage():
    url = "http://www.renren.com/965187997/profile"

    # 如果已经执行了Login函数，则opener自动已经包含相应的cookie值
    rsp = opener.open(url)
    html = rsp.read().decode()

    with open("rsp.html","w") as f:
        f.write(html)

if __name__ == '__main__':
    login()
    getHomepage()
    