'''

破解又到辞典
'''

import urllib.request,urllib.parse

def youdao(key):
    url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"

    data = {
        "i": "girl",
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": "15659619555362",
        "sign": "3481a03ea07b1b290d156d9e10392887",
        "ts": "1565961955536",
        "bv": "50a5db8e0811aeb43003d7bc848e2439",
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_REALTlME"
    }

    data = urllib.parse.urlencode(data).encode()

